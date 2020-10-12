from django.db import models

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digitis=20, defacult=100.00)