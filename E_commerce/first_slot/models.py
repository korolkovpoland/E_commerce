from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField( max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    images = models.ImageField(blank=True, upload_to='images')

    def __str__(self) -> str:
        return self.name