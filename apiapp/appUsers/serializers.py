from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
	
	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = {'first_name', 'last_name', 'mobile_no', 'address', 'email', 'id', 'password'}