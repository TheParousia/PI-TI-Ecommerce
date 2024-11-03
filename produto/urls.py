from django.urls import path
from django.contrib.auth import views as auth_views
from produto.views import atualizar_produtos, excluir_produtos, pagina_adm
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pagina_home, name='pagina_home'),
    path('', views.produtos, name='produtos'), # Verificar validade
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/<int:produto_id>/', views.produto_detalhes, name='produto_detalhes'),
    path('produtos/detalhes/<int:produto_id>', views.detalhesProduto, name="detalhesProdutos"),
    path('produtos/criar/', views.tela_produto,name="tela_produto"),
    
    # Adm de produtos
    path('produtos/listar/', pagina_adm, name='pagina_adm'),  # Listagem de produtos
    path('produtos/atualizar/<int:produto_id>/', atualizar_produtos, name='atualizar_produto'),  # Atualização de produto
    path('produtos/excluir/<int:produto_id>/', excluir_produtos, name='excluir_produto'),  # Exclusão de produto
    
    # Informações da esquipe
    path('add_infor', views.add_infor, name="add_infor"),
]
