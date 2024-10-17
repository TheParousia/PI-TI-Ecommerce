from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import FormularioLogin
from produto.forms import FormularioLogin  # Certifique-se de que o nome do formulário está correto
from .forms import ClienteForm
from django.contrib.auth.hashers import make_password

# views.py
from .models import Cliente

def registrar(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm_password')

        # Valida se a senha e a confirmação de senha coincidem
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'registrar.html')  # Volta para a página de registro

        # Verifica se o email já está cadastrado
        if Cliente.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está em uso. Tente outro.')
            return render(request, 'registrar.html')  # Volta para a página de registro

        # Verifica se o username já está cadastrado
        if Cliente.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso. Tente outro.')
            return render(request, 'registrar.html')  # Volta para a página de registro

        # Cria o cliente (hashing a senha para segurança)
        cliente = Cliente(
            nome=nome,
            username=username,
            email=email,
            telefone=telefone,
            cpf_cnpj=cpf_cnpj,
            cep=cep,
            rua=rua,
            numero=numero,
            bairro=bairro,
            senha=make_password(senha),  # Hasheia a senha corretamente
        )
        cliente.save()

        # Autentica o usuário após registrar
        usuario = authenticate(request, username=username, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('conta_criada')  # Redireciona para a página de sucesso

    # Caso o método não seja POST, renderiza a página de registro
    return render(request, 'registrar.html')

# Create your views here.
def produtos(request):
    return render(request, "produtos.html") 

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
                print("Usuário autenticado: ",usuario.is_authenticated)
                return redirect('produtos')  # Redireciona para a página inicial (ou qualquer outra)
            else:
                # Se as credenciais forem inválidas, exibe uma mensagem de erro
                messages.error(request, 'Nome de usuário ou senha inválidos.')
    else:
        # Se o método não for POST, exibe o formulário vazio
        form = FormularioLogin()

    # Renderiza o template de login com o formulário
    return render(request, 'login_independente.html', {'form': form})


def conta_criada(request):
    return render(request, 'conta_criada.html')  # Página de sucesso após a criação da conta