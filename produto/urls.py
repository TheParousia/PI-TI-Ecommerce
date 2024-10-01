
from django.urls import path
from . import views

urlpatterns = [
    path('produtos/detalhes/<int:produto_id>', views.detalhesProduto, name="detalhesProdutos")
]
