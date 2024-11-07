from rest_framework import serializers
from .models import Venda, ItemVenda, STATUS_CHOICES
from usuario.models import Cliente
from produto.models import Produto

from rest_framework import serializers
from .models import ItemVenda


class ItemCarrinhoSerializer(serializers.ModelSerializer):
    id_produto = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(),
        write_only=True
    )
    quantidade = serializers.IntegerField(min_value=1)

    class Meta:
        model = ItemVenda
        fields = ['id_produto', 'quantidade']

    def create(self, validated_data):

        user = self.context['request'].user
        produto = validated_data['id_produto']
        quantidade = validated_data['quantidade']

        print("Id produto:' ", produto)
        print("Qtd: ", quantidade)

        cliente = Cliente.objects.get(id=user.id)
        venda, craeted = Venda.objects.get_or_create(
            cliente=cliente, status='0')

        if craeted:
            cliente = Cliente.objects.get(id=user.id)
            venda = Venda.objects.create(
                cliente=cliente, status='0')

        venda.save()

        print("Venda:", venda)
        print("Venda id:", venda.id)
        # Checa se o item já está no carrinho do usuário

        try:
            itemCarrinho = ItemVenda.objects.get(
                venda=venda,
                produto=produto,
            )

        except:
            itemCarrinho = ItemVenda()

            itemCarrinho.venda = venda
            itemCarrinho.produto = produto

        itemCarrinho.quantidade = quantidade
        itemCarrinho.preco = produto.preco
        itemCarrinho.total = produto.preco * itemCarrinho.quantidade

        itemCarrinho.save()

        return itemCarrinho
