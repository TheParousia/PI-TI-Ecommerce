from django.contrib import admin
from django.urls import path
from . import views
#from .views import produtos

urlpatterns = [             
path('produtos/', views.produtos, name='produtos'),
path('filtrar/', views.filtrar_produtos, name='filtrar_produtos'),
path('contagem/', views.contar_produtos, name='contar_produtos'),


]

