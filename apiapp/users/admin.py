from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = User
	list_display = ('email', 'is_active', 'is_staff')
	list_filter = ('email', 'is_active', 'is_staff')
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Permissions', {'fields': ('is_staff', 'is_active')})
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)

admin.site.register(User, CustomUserAdmin)

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']