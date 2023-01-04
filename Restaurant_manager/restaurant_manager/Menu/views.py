from django.shortcuts import render
from django.http import HttpResponse

from .forms import InputForm


def menu_disp(request):
    return HttpResponse(""" En esta pantalla se va a mostrar el menu cumpleto, donde venga el nombre, precio y de donde es el platillo.
    tambien tiene que ser dinamico y si le picas a un platillo te muestra las caracteristicas de cada platillo
    """)



    
