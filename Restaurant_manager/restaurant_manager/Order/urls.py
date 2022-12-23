from django.urls import path
from . import views

urlpatterns = [
    path('', views.Make_order, name= 'Make_order')
]