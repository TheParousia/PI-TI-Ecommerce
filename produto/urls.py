from django.urls import path
from .views import produtos, produto_detalhes

urlpatterns = [
    path('produtos/', produtos, name='produtos'),
    path('produtos/<int:produto_id>/', produto_detalhes, name='produto_detalhes'),
]