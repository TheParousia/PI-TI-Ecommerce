from django.db import models

class Produto(models.Model):
    modelo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    capacidade1 = models.CharField(max_length=10)
    capacidade2 = models.CharField(max_length=10)
    capacidade3 = models.CharField(max_length=10)
    qtd_estoque = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cor = models.CharField(max_length=30, default='')
    marca = models.CharField(max_length=30, default='')
    imagem = models.ImageField(upload_to='produto', default='img')
    acessos = models.IntegerField(default=0)  # Adiciona o campo de acessos

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.cor}) - R${self.preco}"