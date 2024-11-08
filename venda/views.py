from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from produto.models import Produto
from usuario.models import Cliente
from venda.models import ItemVenda, Venda
from .serializers import ItemCarrinhoSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.


class AddProdNoCarrinhoAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.data)
        serializer = ItemCarrinhoSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_produto):
        try:

            cliente = Cliente.objects.get(id=request.user.id)

            venda = Venda.objects.get(
                cliente=cliente, status='0'
            )

            if venda is not None:
                # Tenta obter o item do carrinho com base no usuário e no ID do produto
                itemCarrinho = ItemVenda.objects.get(
                    venda=venda, produto=id_produto)

                itemCarrinho.delete()

            return Response({"detail": "Item removido do carrinho com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except ItemVenda.DoesNotExist:
            return Response({"error": "Item não encontrado no carrinho."}, status=status.HTTP_404_NOT_FOUND)


class DeletarDoCarrinhoAPI(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id_produto):
        try:

            cliente = Cliente.objects.get(id=request.user.id)

            venda = Venda.objects.get(
                cliente=cliente, status='0'
            )

            if venda is not None:
                # Tenta obter o item do carrinho com base no usuário e no ID do produto
                itemCarrinho = ItemVenda.objects.get(
                    venda=venda, produto=id_produto)

                itemCarrinho.delete()

            return Response({"detail": "Item removido do carrinho com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except ItemVenda.DoesNotExist:
            return Response({"error": "Item não encontrado no carrinho."}, status=status.HTTP_404_NOT_FOUND)


@login_required
def carrinho(request):

    cliente = Cliente.objects.get(id=request.user.id)

    venda = Venda.objects.get(
        cliente=cliente, status='0'
    )

    itensCarrinho = ItemVenda.objects.filter(
        venda=venda
    )

    contexto = {
        "itensCarrinho": itensCarrinho
    }
    return render(request, 'carrinho.html', contexto)
