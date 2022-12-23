from django.db import models
from unicodedata import name

class Daily_sellM(models.Model):
    Dish = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    Table = models.IntegerField()

