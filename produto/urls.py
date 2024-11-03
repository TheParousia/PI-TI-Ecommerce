from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_home, name='pagina_home'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/<int:produto_id>/', views.produto_detalhes, name='produto_detalhes'),
    path('produtos/detalhes/<int:produto_id>', views.detalhesProduto, name="detalhesProdutos"),
    path('produtos/criar/', views.tela_produto,name="tela_produto"),
    path('add_infor', views.add_infor, name="add_infor"),
]