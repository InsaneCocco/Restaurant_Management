from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu_items


def menu_disp(request):
    newmenu = Menu_items.objects.all()
    newmenu_dict = {'menu' : newmenu}
    return render(request, 'menu.html', newmenu_dict)