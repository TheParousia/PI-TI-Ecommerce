from django.urls import path
from . import views

urlpatterns = [
    path('', views.template, name='template'),
    path('login/', views.login_view, name='login'),  # Rota para a tela de login
    path('registrar/', views.registrar_view, name='registrar'),  # Rota para o registro
]
