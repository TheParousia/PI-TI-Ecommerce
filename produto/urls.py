from django.urls import path
from produto.views import atualizar_produtos, excluir_produtos, pagina_adm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', pagina_adm, name='pagina_adm2'),  # Página inicial de administração
    path('produtos/listar/', pagina_adm, name='pagina_adm'),  # Listagem de produtos
    path('produtos/atualizar/<int:produto_id>/', atualizar_produtos, name='atualizar_produto'),  # Atualização de produto
    path('produtos/excluir/<int:produto_id>/', excluir_produtos, name='excluir_produto'),  # Exclusão de produto
]

# Serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
