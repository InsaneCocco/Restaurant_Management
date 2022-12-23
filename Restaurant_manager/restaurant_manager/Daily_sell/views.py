from django.shortcuts import render
from django.http import HttpResponse

def Daily_sell(request):
    return HttpResponse('Este es el view del daily. En esta app se va a hacer una base de datos de la venta diaria del restaurante')
