from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from produto import views

urlpatterns = [
    path('', views.tela_produto, name="tela_produto"),  # Mantendo apenas a view 'frontend'
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),  # Rota para listar produtos
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
