from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
      
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

      
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cpf_cnpj = models.CharField(max_length=18)  # Pode ser CPF ou CNPJ
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=255)
    senha = models.CharField(max_length=128)  # Considere usar hashing

class Modelo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'


class Cor(models.Model):
    nome = models.CharField(max_length=50)
    codigo_hex = models.CharField(max_length=7)  # Código hexadecimal da cor

    def __str__(self):
        return f"{self.nome} ({self.codigo_hex})"

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'


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
        return f"{self.marca} {self.modelo} - Cor: {self.cor.nome} - R${self.preco:.2f}"


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['marca', 'modelo']  # Ordenar produtos por marca e modelo

