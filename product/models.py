from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price=models.DecimalField()

class Aggregate(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
