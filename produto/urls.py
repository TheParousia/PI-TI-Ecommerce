from django.urls import path
from produto import views

urlpatterns = [
    path('', views.cadastrar_cor, name='cadastrar_cor'),  # Mudado para a função de cadastro de cor
    path('cor_cadastrar_atualizar/', views.cor_cadastrar_atualizar, name='cor_cadastrar_atualizar'),  # Rota para a página de confirmação
    path('cor/deletar/<int:id>', views.cor_deletar, name='cor_deletar'),  # Rota para atualizar cor
    
    path('atualizar-cor/', views.atualizar_cor, name='atualizar_cor'),  # Rota para atualizar cor
]
