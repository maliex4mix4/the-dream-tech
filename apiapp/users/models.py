from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from .managers import UserManager

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
