from django.urls import path
from . import views
from .views import registrar

urlpatterns = [
    path('', views.template, name='template'),
    path('login/', views.login_view, name='login'),  # Rota para a tela de login  
    #path('registrar/', views.registrar_cliente, name='registrar_cliente'), # Rota para o registro
    path('registrar/', registrar, name='registrar'),
]
