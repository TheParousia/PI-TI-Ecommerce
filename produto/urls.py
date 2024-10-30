from django.urls import path
from produto import views

urlpatterns = [
    path('', views.cadastrar_cor, name='cadastrar_cor'),  # Mudado para a função de cadastro de cor
    path('cor_atualizada/', views.cor_atualizada, name='cor_atualizada'),  # Rota para a página de confirmação
    path('atualizar-cor/', views.atualizar_cor, name='atualizar_cor'),  # Rota para atualizar cor
]
