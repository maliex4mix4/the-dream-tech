from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime
from datetime import timedelta

# Create your models here.

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)

class UserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError(_('The email must be given'))
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Superuser must be a staff.'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_("Ops! you have to be a Superuser"))
		return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
 	username = None
 	phone_no = models.CharField(max_length=50, unique=True)
 	address = models.CharField(max_length=100)
 	email = models.EmailField(_('email address'), unique=True)

 	USERNAME_FIELD = 'email'
 	REQUIRED_FIELDS = ['first_name', 'last_name', 'address', 'phone_no']

 	objects = UserManager()

 	def __str__(self):
 		return self.email


class EmailActivationQuerySet(models.query.QuerySet):

    def confirmable(self):
        """
        Returns those emails which can be confirmed i.e. which are not activated and expired
        """
        now = timezone.now()
        start_range = now - timedelta(days=DEFAULT_ACTIVATION_DAYS)
        end_range = now
        return self.filter(
            activated=False,
            forced_expire=False
        ).filter(
            timestamp__gt=start_range,
            timestamp__lte=end_range
        )


class EmailActivationManager(models.Manager):

    def get_queryset(self):
        return EmailActivationQuerySet(self.model, using=self._db)

    def confirmable(self):
        return self.get_queryset().confirmable()

    def email_exists(self, email):
        """
        EmailActivation is created when the user is created. When only EmailActivation is deleted, User object
        still remains i.e. email still exists. But this function will send nothing because for this function
        self.get_queryset() is None. So both user and EmailActivation should exist together for this to work.
        """
        return self.get_queryset().filter(
            Q(email=email) | Q(user__email=email)
        ).filter(activated=False)


class EmailActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    key = models.CharField(max_length=120, blank=True, null=True)  # activation key
    activated = models.BooleanField(default=False)
    forced_expire = models.BooleanField(default=False)  # link expired manually
    expires = models.IntegerField(default=7)  # automatic expire (after days)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = EmailActivationManager()

    def __str__(self):
        return self.email

    def can_activate(self):
        # A custom queryset was created because now a particular object can be checked directly
        # without first fetching the instance
        qs = EmailActivation.objects.filter(pk=self.pk).confirmable()
        if qs.exists():
            return True
        return False

    def activate(self):
        if self.can_activate():
            # TODO: pre_save that user is activated (do something with this info)
            user = self.user
            user.is_active = True
            user.save()
            # TODO: post_save user activation signal (do something with this info)
            self.activated = True
            self.save()
            return True
        return False

    def regenerate(self):
        self.key = None
        self.save()
        if self.key is not None:
            return True
        return False

    def send_activation(self):
        if not self.activated and not self.forced_expire:
            if self.key:
                base_url = getattr(settings, 'HOST_SCHEME') + getattr(settings, 'BASE_URL')
                key_path = reverse('account:email-activate', kwargs={'key': self.key})
                path = '{base}{path}'.format(base=base_url, path=key_path)
                context = {
                    'path': path,
                    'email': self.email
                }
                txt_ = get_template('email_verify.txt').render(context)
                html_ = get_template('email_verify.html').render(context)
                subject = 'XYZ - Verify your Account'
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [self.email]
                sent_mail = send_mail(
                    subject,
                    txt_,  # If content_type is text/plain
                    from_email,
                    recipient_list,
                    html_message=html_,  # If content_type is text/html
                    fail_silently=False  # If false, then an email will be sent if error occurs while sending the email
                )
                return sent_mail
        return False
