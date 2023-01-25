from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = (models.CharField(max_length=25))
    # como es FK de otros modelos se tiene que llenar antes que los demas modelos.

    def __str__(self) -> str:
        return self.country_name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class Ingredients(models.Model):
    ingr_name = (models.CharField(max_length=20))
    ingr_type = (models.CharField(max_length=20)) # especificar si es especia, fruto, proteina, etc.
    country = (models.ForeignKey(Country, on_delete= models.CASCADE, related_name= 'ingredients'))

    def __str__(self) -> str:
        return self.ingr_name

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
    
class Menu_items(models.Model):
    dish_name = (models.CharField(max_length=30))
    country = (models.ForeignKey(Country, on_delete= models.CASCADE, related_name= 'Menu'))
    price = (models.IntegerField(default= 100))

    def __str__(self) -> str:
        return self.dish_name

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

class Characteristict(models.Model):
    dish_name = (models.ForeignKey(Menu_items, on_delete=models.CASCADE, related_name='Caracteristict'))
    # este modelo va a mostrar una tabla de cada una de las caracteristicas de los platillos. probablemente se tenga que cambiar a una dinamica porque va a haber muchos platillos
    class Meta:
        verbose_name = 'Characteristic'
        verbose_name_plural = 'Characteristics'
    # practicar como agregar datos a las tablas y despues obtener los datos de la shell




