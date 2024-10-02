from django.contrib import admin
from django.urls import path
from produto.views import pagina_home

urlpatterns = [
    path('', pagina_home, name='pagina_home'),
]
