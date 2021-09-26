"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import forms
from django.contrib import admin
from django.urls import path
from app.views import create_empresas, create_produtos, forms_empresas, forms_produtos, home, home_produtos, view_empresas, view_produtos, edit_empresas, edit_produtos, update_empresas, update_produtos, delete_empresas, delete_produtos, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path(' ', index),
    path('home/', home, name='home'),
    path('home_produtos/', home_produtos, name='home_produtos'),
    path('forms_empresas/', forms_empresas, name='forms_empresas'),
    path('forms_produtos/', forms_produtos, name='forms_produtos'),
    path('create_empresas/', create_empresas, name='create_empresas'),
    path('create_produtos/', create_produtos, name='create_produtos'),
    path('view_empresas/<int:pk>/', view_empresas, name='view_empresas'),
    path('view_produtos/<int:pk>/', view_produtos, name='view_produtos'),
    path('edit_empresas/<int:pk>/', edit_empresas, name='edit_empresas'),
    path('edit_produtos/<int:pk>/', edit_produtos, name='edit_produtos'),
    path('update_empresas/<int:pk>/', update_empresas, name='update_empresas'),
    path('update_produtos/<int:pk>/', update_produtos, name='update_produtos'),
    path('delete_empresas/<int:pk>/', delete_empresas, name='delete_empresas'),
    path('delete_produtos/<int:pk>/', delete_produtos, name='delete_produtos')
    
    

]
