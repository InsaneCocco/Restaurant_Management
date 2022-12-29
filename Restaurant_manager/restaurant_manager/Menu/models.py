from django.db import models

# Create your models here.
class Menu_items(models.Model):
    dish_name = (models.CharField(max_length=30))

class Country(models.Model):
    country_name = (models.CharField(max_length=25))
    dish_name = models.ForeignKey(Menu_items, on_delete= models.CASCADE, related_name='Country')
    