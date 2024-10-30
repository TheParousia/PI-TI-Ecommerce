from django.contrib import admin
from django.urls import path
from produto.views import pagina_home, views

urlpatterns = [
    path('', pagina_home, name='pagina_home'),    
    path('produtos/detalhes/<int:produto_id>',
         views.detalhesProduto, name="detalhesProdutos"),
    path('produtos/criar/', views.tela_produto,
         name="tela_produto"),  # Tela de produto
    path('add_infor', views.add_infor, name="add_infor"),
]