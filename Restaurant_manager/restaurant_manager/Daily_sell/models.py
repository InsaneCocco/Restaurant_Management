from django.db import models
from unicodedata import name

from Employees.models import Waiter

class Daily_sellM(models.Model):
    Table = models.IntegerField()
    waiter = (models.ForeignKey(Waiter, on_delete= models.CASCADE, related_name= 'waiter'))
    Dish = models.CharField(max_length=50)
    Quantity = models.IntegerField()