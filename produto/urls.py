from django.contrib import admin
from django.urls import path
from produto import views

urlpatterns = [
    path('produtos/', views.home, name="home"),
    path('produtos/detalhes/<int:id>', views.detalhesProduto, name="detalhesProduto"),
]
