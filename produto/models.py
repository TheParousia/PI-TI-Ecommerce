# models.py
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    cpf_cnpj = models.CharField(max_length=18)  # Altere conforme a necessidade
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=255)
    senha = models.CharField(max_length=128)  # Você pode usar hashing depois

    def __str__(self):
        return self.nome
