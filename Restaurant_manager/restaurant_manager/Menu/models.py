from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = (models.CharField(max_length=25))

class Ingredients(models.Model):
    ingr_name = (models.CharField(max_length=20))
    ingr_type = (models.CharField(max_length=20)) # especificar si es especia, fruto, proteina, etc.
    country = (models.ForeignKey(Country, on_delete= models.CASCADE, related_name= 'ingredients'))
    
class Menu_items(models.Model):
    dish_name = (models.CharField(max_length=30))
    country = (models.ForeignKey(Country, on_delete=models.CASCADE, related_name= ' Menu'))