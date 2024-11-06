from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rota via API
    path(
        'carrinho/add/',
        views.AddProdNoCarrinhoAPI.as_view()
    ),
    path(
        'carrinho/delete/<int:id_produto>/',
        views.AddProdNoCarrinhoAPI.as_view()
    ),

    # Rota via Template
    path('carrinho/', views.carrinho, name='carrinho'),
    # path('carrinho/add/', views.ItemCreateView.as_view()),
    # path('carrinho/adicionar/', views.adicionarAoCarrinho),
    # path('carrinho/', views.login_view, name='login'),
    # path('vendas/listar', auth_views.LogoutView.as_view(), name='logout'),
    # path('vendas/detalhes/<int:venda_id>/',
    #      views.conta_criada, name='conta_criada'),
    # path('registrar/', views.registrar, name='registrar'),
]
