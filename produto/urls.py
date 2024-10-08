from django.contrib import admin
from django.urls import path
from produto.views import pagina_home, atualizar_produtos, excluir_produtos, criar_produtos, pagina_adm

urlpatterns = [
    path('', pagina_adm, name='pagina_adm2'),  # Pagina inicial
    path('produtos/listar', pagina_adm, name='pagina_adm'),  # Pagina inicial de lista de produtos
    path('produtos/criar/', criar_produtos, name='criar_produto'),  # Pagina para criar novo produto
    path('produtos/atualizar/<int:produto_id>/', atualizar_produtos, name='atualizar_produto'),  # Atualizar produto
    path('produtos/deletar/<int:produto_id>/', excluir_produtos, name='deletar_produto'),  # Deletar produto
    path('admin/', admin.site.urls),  # Rota para o painel de admin
]
