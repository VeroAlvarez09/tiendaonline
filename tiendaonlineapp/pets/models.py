from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    value = models.FloatField(default=0)
    image = models.ImageField()
    active = models.BooleanField(default=1)