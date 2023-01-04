from django.shortcuts import render
from django.http import HttpResponse

from .forms import InputForm


def emp_home(request):
    return HttpResponse('On this view will dsplay all the matter with the employees')

def form_view(request):
    form = InputForm()
    context = {'form' : form}
    return render(request, 'home.html', context)