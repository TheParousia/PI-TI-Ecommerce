from django.urls import path
from django.contrib.auth import views as auth_views
from produto.views import atualizar_produtos, excluir_produtos, pagina_adm
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('atualizar-cor/', views.atualizar_cor, name='atualizar_cor'),  # Rota para atualizar cor
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
    
    # Adm Cores
    path('cor/listar', views.cadastrar_cor, name='cadastrar_cor'),  # Mudado para a função de cadastro de cor
    path('cor/cadastrar_atualizar/', views.cor_cadastrar_atualizar, name='cor_cadastrar_atualizar'),  # Rota para a página de confirmação
    path('cor/deletar/<int:id>', views.cor_deletar, name='cor_deletar'),  # Rota para atualizar cor  

    # Informações da esquipe
    path('add_infor', views.add_infor, name="add_infor"),
]
