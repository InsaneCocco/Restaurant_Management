from django.urls import path
from . import views

urlpatterns = [
    path('', views.Daily_sell, name='Daily'),

]