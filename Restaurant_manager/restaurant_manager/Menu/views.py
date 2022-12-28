from django.shortcuts import render
from django.http import HttpResponse


def menu_disp(request):
    return HttpResponse('Here will be displayed the menu')
    