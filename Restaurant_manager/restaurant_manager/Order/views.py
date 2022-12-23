from django.shortcuts import render
from django.http import HttpResponse

def Make_order(request):
    return HttpResponse(' en este view se van a realizar las ordenes de las mesas')
    #realizar una model para cada mesa, en donde se especifique mesa para cuantos es, pedidos, precios, etc
    