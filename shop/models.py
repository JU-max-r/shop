from django.db import models

class Product(models.Model):
    price = models.PositiveIntegerField()
    stocks = models.PositiveSmallIntegerField()
    cost = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to ='images/')
    description = models.TextField()
    count = models.PositiveIntegerField()
    dicount = models.IntegerField()
    rating = models.PositiveIntegerField()
    material = models.CharField(max_length=30)
    brand = models.CharField(max_length=20) 



