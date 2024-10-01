from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from produto import views

urlpatterns = [
    path('', views.listar_cartao, name="listar_cartao"),
    path('formulario_post/', views.formulario_post, name="formulario_post"),
    path('deletar/<int:id>/', views.deletar_cartao, name="deletar_cartao"),
    path('atualizar/<int:id>/', views.atualizar_cartao, name="atualizar_cartao"),
    path('pagina2/', views.pagina2, name="clark"),
    path('formulario/', views.formulario, name="formulario"),
    path('frontend/', views.frontend, name="frontend"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
