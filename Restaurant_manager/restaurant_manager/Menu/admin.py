from django.contrib import admin
from .models import Menu_items, Country, Ingredients, Characteristict

# Register your models here. 
admin.site.register(Country)
admin.site.register(Ingredients)
admin.site.register(Menu_items)
admin.site.register(Characteristict)