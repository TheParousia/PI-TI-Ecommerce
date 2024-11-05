from django.db import models
from produto.models import Produto

# Create your models here.


class Venda(models.Model):
    user_id = models.ForeignKey(, on_delete=models.CASCADE)
    ultima_modificacao = models.DateTimeField(auto_now=True)
    status = models.TextChoices(
        'status', 'CARRINHO EMITIDA CANCELADA FINALIZADA')


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
