
from django.urls import path
from . import views

urlpatterns = [
    path('', views.detalhesProduto, name="detalhesProdutos"),
    # path('produtos/detalhes/<int:produto_id>', views.detalhesProduto, name="detalhesProdutos"),
    path('add_infor', views.add_infor, name="add_infor"),
]
    