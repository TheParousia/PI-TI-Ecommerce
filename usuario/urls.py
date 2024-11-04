from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Rota para a tela de login  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('conta-criada/', views.conta_criada, name='conta_criada'),
    path('registrar/', views.registrar, name='registrar'),
]
