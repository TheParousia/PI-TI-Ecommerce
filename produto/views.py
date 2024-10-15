from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import FormularioLogin
from produto.forms import FormularioLogin  # Certifique-se de que o nome do formulário está correto
from .forms import ClienteForm

# views.py
from .models import Cliente

def registrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        senha = request.POST.get('password')  # Aqui você deve aplicar hashing

        # Salva o novo cliente no banco de dados
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
            senha=senha,  # Não esqueça de hashear a senha!
        )
        cliente.save()
        return redirect('alguma_url_de_sucesso')  # Altere para a URL desejada

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


def registrar_view(request):
    if request.method == 'POST':
        # Lógica para registrar o usuário aqui
        pass
    return render(request, 'registrar.html')  # Certifique-se de que você tem um template registrar.html
