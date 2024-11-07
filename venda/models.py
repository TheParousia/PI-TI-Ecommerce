from django.db import models
from produto.models import Produto
from usuario.models import Cliente

# Create your models here.
STATUS_CHOICES = [
    ('0', 'CARRINHO'),
    ('1', 'EMITIDA'),
    ('2', 'CANCELADA'),
    ('3', 'FINALIZADA'),
]

# Definindo o campo com choices


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ultima_modificacao = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='0',  # valor padrão, opcional
    )


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
