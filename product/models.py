from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    description=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Aggregate(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name