from django.shortcuts import render
from django.http import HttpResponse


def menu_disp(request):
    return HttpResponse(""" En esta pantalla se va a mostrar el menu cumpleto, donde venga el nombre, precio y de donde es el platillo
    """)
    