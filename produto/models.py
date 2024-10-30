from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cor(models.Model):
    nome = models.CharField(max_length=50)
    codigo_hex = models.CharField(max_length=7)  # Adicionando campo para o código hexadecimal da cor

    def __str__(self):
        return f"{self.nome} ({self.codigo_hex})"  # Exibindo o nome e o código hexadecimal

class Produto(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    capacidade1 = models.CharField(max_length=10)
    capacidade2 = models.CharField(max_length=10)
    capacidade3 = models.CharField(max_length=10)
    qtd_estoque = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagem1 = models.ImageField(upload_to='produto', default='img/default.jpg')
    imagem2 = models.ImageField(upload_to='produto', default='img/default.jpg')
    imagem3 = models.ImageField(upload_to='produto', default='img/default.jpg')
    imagem4 = models.ImageField(upload_to='produto', default='img/default.jpg')
    acessos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.marca} {self.modelo} - Cor: {self.cor.nome} - R${self.preco:.2f}"  # Exibindo informações detalhadas
