from django.contrib import admin
from django.urls import path
from . import views
#from .views import produtos

urlpatterns = [             
path('produtos/', views.produtos, name='produtos'),
]

