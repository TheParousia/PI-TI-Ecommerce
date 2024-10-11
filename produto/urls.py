from django.contrib import admin
from django.urls import path
from produto.views import atualizar_produtos, excluir_produtos, pagina_adm

urlpatterns = [
    path('', pagina_adm, name='pagina_adm2'),
    path('produtos/listar/', pagina_adm, name='pagina_adm'),
    path('produtos/atualizar/<int:produto_id>/', atualizar_produtos, name='atualizar_produto'),
    path('produtos/excluir/<int:produto_id>/', excluir_produtos, name='excluir_produto'),
]