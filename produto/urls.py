from django.urls import path
from produto import views

urlpatterns = [
  path('', views.tela_produto, name="tela_produto"),  # Tela de produto   
  path('produtos/detalhes/<int:produto_id>', views.detalhesProduto, name="detalhesProdutos"),
  path('produtos/criar/', views.tela_produto, name="tela_produto"),  # Tela de produto
  path('add_infor', views.add_infor, name="add_infor"),
  path('admin/', admin.site.urls),
]