from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    remetente = models.CharField(max_length=30)
    mensagem = models.CharField(max_length=255)
    #capacidade1 = models.IntegerField()
    #capacidade2 = models.IntegerField()
    #capacidade3 = models.IntegerField()
    imagem = models.ImageField(default='')  # Campo para imagem

    