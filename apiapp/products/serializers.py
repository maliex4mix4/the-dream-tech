from rest_framework import serializers
from .models import Products
from .models import Category

def ProductsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
