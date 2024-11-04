from django.urls import path
from produto import views

urlpatterns = [
    path('', views.cadastrar_marca, name='cadastrar_marca'),  # Página de cadastro de marca
    path('marca/cadastrar-atualizar/', views.marca_cadastrar_atualizar, name='marca_cadastrar_atualizar'),  # Rota para cadastrar ou atualizar marca
    path('marca/deletar/<int:id>/', views.marca_deletar, name='marca_deletar'),  # Rota para deletar marca
    path('atualizar-marca/', views.atualizar_marca, name='atualizar_marca'),  # Rota para visualizar marcas e suas informações
]
