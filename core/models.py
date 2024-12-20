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

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.cor}) - R${self.preco}"

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cor(models.Model):
    nome = models.CharField(max_length=100)
    codigo_hex = models.CharField(max_length=7)  # Código hexadecimal da cor

    def __str__(self):
        return self.nome