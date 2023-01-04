from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form_view, name = 'form_view' ),
    path('', views.emp_home, name = 'emp_home' ),

]