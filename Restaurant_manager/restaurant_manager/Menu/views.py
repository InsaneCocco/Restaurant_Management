from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu_items

# def menu_disp(request):
#     about_content = { 'about' : " En esta pantalla se va a mostrar el menu cumpleto, donde venga el nombre, precio y de donde es el platillo. tambien tiene que ser dinamico y si le picas a un platillo te muestra las caracteristicas de cada platillo"}
#     return render(request, 'menu.html', about_content)


def menu_disp(request):
    newmenu = Menu_items.objects.all()
    newmenu_dict = {'menu' : newmenu}
    return render(request, 'menu.html', newmenu_dict)