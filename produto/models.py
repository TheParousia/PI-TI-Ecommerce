from django.db import models

class Produto(models.Model):
    modelo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)  # Corrigi a acentuação
    capacidade1 = models.CharField(max_length=10)  # Usei CharField em vez de TextField para capacidade
    capacidade2= models.CharField(max_length=10)  # Usei CharField em vez de TextField para capacidade
    capacidade3 = models.CharField(max_length=10)  # Usei CharField em vez de TextField para capacidade
    qtdEstoque = models.IntegerField(default=0)  # Usei IntegerField para quantidade de estoque
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Usei DecimalField para preco
    cor = models.CharField(max_length=30, default='')  # Usei CharField para cor
    marca = models.CharField(max_length=30, default='')  # Usei CharField para marca

