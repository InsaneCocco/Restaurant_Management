from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = (models.CharField(max_length=25))
    # como es PK de otros modelos se tiene que llenar antes que los demas modelos.

class Ingredients(models.Model):
    ingr_name = (models.CharField(max_length=20))
    ingr_type = (models.CharField(max_length=20)) # especificar si es especia, fruto, proteina, etc.
    country = (models.ForeignKey(Country, on_delete= models.CASCADE, related_name= 'ingredients'))
    
class Menu_items(models.Model):
    dish_name = (models.CharField(max_length=30))
    country = (models.ForeignKey(Country, on_delete= models.CASCADE, related_name= 'Menu'))
    price = (models.IntegerField(default= 100))

class Caracteristict(models.Model):
    dish_name = (models.ForeignKey(Menu_items, on_delete=models.CASCADE, related_name='Caracteristict'))
    # este modelo va a mostrar una tabla de cada una de las caracteristicas de los platillos. probablemente se tenga que cambiar a una dinamica porque va a haber muchos platillos

    # practicar como agregar datos a las tablas y despues obtener los datos de la shell
    # practicar como hacer merge y pull request para poder hacer commits en git



