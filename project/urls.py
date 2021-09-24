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
from django.contrib import admin
from django.urls import path
from app.views import create_empresas, delete_empresa, edit_empresas, form_empresas, home, form, create, update_empresas, view, edit, update, delete, form, view_empresas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('forms/', form, name='forms'),
    path('create/', create, name='create'),
    path('create_empresas/', create_empresas, name='create_empresas'),
    path('view/<int:pk>/', view, name='view'),
    path('view_empresas/<int:pk>/', view_empresas, name='view_empresas'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('edit_empresas/<int:pk>/', edit_empresas, name='edit_empresas'),
    path('update/<int:pk>/', update, name='update'),
    path('update_empresas/<int:pk>/', update_empresas, name='update_empresas'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('delete_empresa/<int:pk>/', delete_empresa, name='delete_empresa'),
    path('forms_empresa/', form_empresas, name='form_empresas'),


]
