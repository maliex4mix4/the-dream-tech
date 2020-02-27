from .models import User
from rest_framework.serializers import ModelSerializer
from .models import VendorsAccount

class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
		read_only_fields = ('id',)

class VendorSerializer(ModelSerializer):
	class Meta:
		model = VendorsAccount
		fields = '__all__'
		read_only_fields = ('id',)
