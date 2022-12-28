from django.db import models

# Create your models here.
class Menu_items(models.Model):
    dish_name(models.CharField(max_length=30))
    