from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from .models import User

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = User
		fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

	class Meta(UserChangeForm):
		model = User
		fields = ('email',)