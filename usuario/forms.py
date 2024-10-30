from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())  # Campo de senha

    class Meta:
        model = Cliente
        fields = ['nome', 'username', 'email', 'telefone', 'cpf_cnpj', 'cep', 'rua', 'numero', 'bairro', 'senha']

class FormularioLogin(forms.Form):
    nome_usuario = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',
            'placeholder': 'Nome de Usuário'  # Adiciona o placeholder
        })
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control rounded-pill',
            'placeholder': 'Senha'  # Adiciona o placeholder
        })
    )
