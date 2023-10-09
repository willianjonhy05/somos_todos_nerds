"""
URL configuration for stn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import todos, detalhar, sugerir, atualizar, apagar, sobre

urlpatterns = [
    path('', todos, name='todos'),
    path('<int:id>', detalhar, name='detalhar'),
    path('sugerir/', sugerir, name='sugerir'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('deletar/<int:id>', apagar, name='apagar')
   
]