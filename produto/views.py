from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import FormularioLogin
from produto.forms import FormularioLogin  # Certifique-se de que o nome do formulário está correto

# Create your views here.
def template(request):
    return render(request, "template.html") 

def login_view(request):
    form = FormularioLogin()
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            # Obtém os dados do formulário
            nome_usuario = form.cleaned_data['nome_usuario']
            senha = form.cleaned_data['senha']

            # Tenta autenticar o usuário com os dados fornecidos
            usuario = authenticate(request, username=nome_usuario, password=senha)
            if usuario is not None:
                # Se a autenticação for bem-sucedida, faz login e redireciona
                login(request, usuario)
                return redirect('home')  # Redireciona para a página inicial (ou qualquer outra)
            else:
                # Se as credenciais forem inválidas, exibe uma mensagem de erro
                messages.error(request, 'Nome de usuário ou senha inválidos.')
    else:
        # Se o método não for POST, exibe o formulário vazio
        form = FormularioLogin()

    # Renderiza o template de login com o formulário
    return render(request, 'login_independente.html', {'form': form})


def registrar_view(request):
    if request.method == 'POST':
        # Lógica para registrar o usuário aqui
        pass
    return render(request, 'registrar.html')  # Certifique-se de que você tem um template registrar.html
