from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255)
    fullname = models.TextField(nullable=False)
    mobile_no = models.CharField(max_length=255)

class Vendors(models.Model):
	"""docstring for Vendors"""
	address = models.CharField(max_length=255)
    fullname = models.TextField(nullable=False)
    biz_no = models.CharField(max_length=255)
    biz_email = models.EmailField()
    biz_name = models.TextField()
    biz_description = models.CharField(max_length=255)