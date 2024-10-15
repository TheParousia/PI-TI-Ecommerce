from django.urls import path
from . import views
from .views import registrar
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('login/', views.login_view, name='login'),  # Rota para a tela de login  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('registrar/', views.registrar_cliente, name='registrar_cliente'), # Rota para o registro
    path('registrar/', registrar, name='registrar'),
]
