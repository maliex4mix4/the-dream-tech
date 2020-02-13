from .models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
		read_only_fields = ('id',)