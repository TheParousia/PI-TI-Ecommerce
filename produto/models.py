from django.db import models
import os
from django.conf import settings
'''
class clark(models.Model):
    nome = models.CharField(max_length=30)
    remetente = models.CharField(max_length=30)
    mensagem = models.TextField(max_length=255)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return self.nome

    def delete(self, *args, **kwargs):
        # Remove a imagem do sistema de arquivos se existir
        if self.imagem:
            try:
                if os.path.isfile(self.imagem.path):
                    os.remove(self.imagem.path)
            except Exception as e:
                print(f'Erro ao deletar arquivo {self.imagem.path}: {e}')
        
        # Chama o método delete da classe pai
        super().delete(*args, **kwargs)

'''