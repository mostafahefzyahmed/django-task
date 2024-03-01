from django.db import models
from category.models import *
# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField()
    image = models.ImageField(upload_to="photos/%y/%m/%d" , null=True ,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    
def __str__(self):
        return self.name