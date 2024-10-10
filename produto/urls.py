from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from produto import views

urlpatterns = [
    path('', views.tela_produto, name="tela_produto"),  # Tela de produto
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
