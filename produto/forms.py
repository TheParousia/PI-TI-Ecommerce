from django import forms

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
