from django.db import models
from users.models import User
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)
    datecreated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    datecreated = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    discount = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discription = models.CharField(max_length=200)
    img = models.FileField(blank=False, null=False)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
