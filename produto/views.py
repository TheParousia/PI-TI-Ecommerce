from django.shortcuts import render, redirect, get_object_or_404
from .models import Cor
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib import messages
from usuario.forms import FormularioLogin, ClienteForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from produto import models
from .models  import Cor, Marca, Modelo, Produto
from multiprocessing import context

fs = FileSystemStorage()

# views.py
from django.contrib import messages

# View para cadastrar uma nova marca
def cadastrar_marca(request):
    marcas = Marca.objects.all()  # Busca todas as marcas no banco de dados

    if request.method == 'POST':
        nome = request.POST.get('nome')  # Pega apenas o nome

        # Verifica se o campo nome foi preenchido corretamente
        if nome:  
            nova_marca = Marca(nome=nome)  # Cria uma nova instância de Marca
            nova_marca.save()  # Salva a nova marca no banco de dados
            messages.success(request, "Marca cadastrada com sucesso!")  # Mensagem de sucesso
            return redirect('cadastrar_marca')  # Redireciona para a página de cadastro de marca

        messages.error(request, "Por favor, preencha todos os campos.")  # Mensagem de erro

    contexto = {
        "marcas": marcas  # Passa todas as marcas para o template
    }

    return render(request, "cadastrar_marca.html", contexto)  # Renderiza a página de cadastro

# View para atualizar a marca (mostra todas as marcas cadastradas)
def atualizar_marca(request):
    marcas = Marca.objects.all()  # Busca todas as marcas do banco de dados
    return render(request, "atualizar_marca.html", {"marcas": marcas})  # Renderiza a página de atualização com as marcas

# View para cadastrar ou atualizar uma marca
def marca_cadastrar_atualizar(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        nome = request.POST.get("nome")  # Apenas verifica o campo nome

        if id and id != "-1":  # Se o id for diferente de -1, significa que é uma atualização
            marca = get_object_or_404(Marca, id=id)  # Busca a marca no banco de dados
            marca.nome = nome  # Atualiza o nome da marca
            marca.save()  # Salva as alterações no banco de dados
            messages.success(request, "Marca atualizada com sucesso!")  # Mensagem de sucesso
        else:
            # Se o id for -1 ou não estiver presente, significa que é um novo cadastro
            if nome:  # Apenas verifica o campo nome
                nova_marca = Marca(nome=nome)  # Cria uma nova instância de Marca
                nova_marca.save()  # Salva a nova marca no banco de dados
                messages.success(request, "Marca cadastrada com sucesso!")  # Mensagem de sucesso
            else:
                messages.error(request, "Por favor, preencha todos os campos.")  # Mensagem de erro

    return redirect('cadastrar_marca')  # Redireciona de volta para a página de cadastro

# View para deletar uma marca
def marca_deletar(request, id):
    marca = get_object_or_404(Marca, id=id)  # Obtém a marca a ser deletada
    marca.delete()  # Deleta a marca
    messages.success(request, "Marca deletada com sucesso!")  # Mensagem de sucesso
    return redirect('cadastrar_marca')  # Redireciona de volta para a página de cadastro de marcas

def menu_adm(request):
    return render(request, 'menu_adm.html')


def cadastrar_cor(request):
    cores = Cor.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        codigo_hex = request.POST.get('codigo_hex')

        if nome and codigo_hex:
            nova_cor = Cor(nome=nome, codigo_hex=codigo_hex)
            nova_cor.save()  # Salva a nova cor no banco de dados
            messages.success(request, "Cor cadastrada com sucesso!")  # Mensagem de sucesso
            return redirect('atualizar_cor')  # Redireciona para a página de atualização de cor

        messages.error(request, "Por favor, preencha todos os campos.")  # Mensagem de erro

    contexto = {
        "cores": cores
    }

    return render(request, "cadastrar_cor.html", contexto)  # Renderiza a página de cadastro

def atualizar_cor(request):
    cores = Cor.objects.all()  # Busca todas as cores do banco de dados
    return render(request, "atualizar_cor.html", {"cores": cores})  # Renderiza a página de atualização com as cores

def cor_cadastrar_atualizar(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        codigo_hex = request.POST.get("codigo_hex")

        print("id: ", id)

        if id != "-1":
            print("Atualizar")
            
            cor = get_object_or_404(Cor, id=id)

            cor.nome = request.POST.get("nome")
            cor.codigo_hex = request.POST.get("codigo_hex")

            cor.save()
            
        else:
            if nome and codigo_hex:
                nova_cor = Cor(nome=nome, codigo_hex=codigo_hex)
                nova_cor.save()  # Salva a nova cor no banco de dados
                messages.success(request, "Cor cadastrada com sucesso!")  # Mensagem de sucesso

         
    
    return redirect('cadastrar_cor')  # Redireciona para a página de atualização se não for uma requisição POST

def cor_deletar(request, id):  # Obtém a cor selecionada
    cor = get_object_or_404(Cor, id=id)
    cor.delete()
    
    return redirect('cadastrar_cor')  # Redireciona para a página de atualização se não for uma requisição POST

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

def produtos(request):
    # Obtendo os parâmetros de consulta
    marca_id = request.GET.get('marca')
    cor_id = request.GET.get('cor')
    preco_min = float(request.GET.get('precoMin', 0))
    preco_max = float(request.GET.get('precoMax', 10000))
    ordenar_por = request.GET.get('ordenar_produto')
    
    print("ordenar_por: ",ordenar_por)
    
    if preco_min - preco_max < 10:
        preco_min = 0
        preco_max = 10000
    
    precoMin = 0
    precoMax = 10000
    
    
    
    if preco_min != None:
        precoMin = preco_min
        precoMax = preco_max
    
    
    print("preco_min: ",preco_min)
    print("preco_max: ",preco_max)

    # Filtra produtos com preço maior que 100 e menor que 500
    # produtos_precos = Produto.objects.filter(preco__gt=preco_min, preco__lt=preco_max)

    produtos = Produto.objects.all()

    print("Id da marca: ", marca_id)

    # Filtragem
    if marca_id:
        produtos = produtos.filter(marca_id=marca_id)
    if cor_id:
        produtos = produtos.filter(cor_id=cor_id)

    # Validação dos preços
    try:
        preco_min = float(preco_min)
        preco_max = float(preco_max)
    except ValueError:
        preco_min, preco_max = 0, 10000  # Valores padrão em caso de erro

    produtos = produtos.filter(preco__gte=preco_min, preco__lte=preco_max)

    # Ordenação
    if ordenar_por == 'preco_asc':
        produtos = produtos.order_by('preco')
    elif ordenar_por == 'preco_desc':
        produtos = produtos.order_by('-preco')

    total_produtos = produtos.count()

    context = {
        'produtos': produtos,
        'total_produtos': total_produtos,
        'marcas': Marca.objects.all(),
        'cores': Cor.objects.all(),
        'marca_selecionada': marca_id,
        'cor_selecionada': cor_id,
        'preco_min': preco_min,
        'preco_max': preco_max,
        'ordenar_por': ordenar_por,
        "precoMin": precoMin,
        "precoMax": precoMax,
    }

    return render(request, 'produtos.html', context)

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.acessos += 1
    produto.save()
    
    return render(request, 'produto_detalhes.html', {'produto': produto})

    return render(request, 'produtos.html', context)

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.acessos += 1
    produto.save()
    
    return render(request, 'produto_detalhes.html', {'produto': produto})

def detalhesProduto(request, produto_id):
    # Tenta buscar o produto pelo ID ou retorna um erro 404 se não encontrado
    produto = get_object_or_404(Produto, id=produto_id)
    produto.acessos += 1
    produto.save()    

    # Dados do produto a serem passados para o template
    context = {
        'produto': produto
    }
    # Renderiza o template 'produto_detalhes.html' com o contexto do produto
    return render(request, 'produto_detalhes.html', context)

    # return HttpResponse("template.render()")

def pagina_home(request):
    return render(request, 'pagina_home.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')
def pagina_adm(request):
    produtos = Produto.objects.all()
    return render(request, 'pagina_adm.html', {'produtos': produtos})

def excluir_produtos(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('pagina_adm')
    return render(request, 'excluir_produtos.html', {'produto': produto})

def atualizar_produtos(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        #paramos aqui fresco

        nomeModelo = request.POST.get('modelo', produto.modelo)
        
        modelo = Modelo()
        modelo.nome = nomeModelo
        modelo.save()

        produto.modelo = modelo

        idCor = int(request.POST.get('cor', produto.cor))
        cor = Cor.objects.get(id=idCor)

        # produto.cor = Cor.objects.get(nome=nomeCor)
        produto.cor = cor
        
        
        idMarca = request.POST.get('marca', produto.marca)
        marca = Marca.objects.get(id=idMarca)
        

        produto.marca = marca


        produto.descricao = request.POST.get('descricao', produto.descricao)
        produto.capacidade1 = request.POST.get('capacidade1', produto.capacidade1)
        produto.capacidade2 = request.POST.get('capacidade2', produto.capacidade2)
        produto.capacidade3 = request.POST.get('capacidade3', produto.capacidade3)
        
        # Convertendo qtd_estoque para inteiro
        produto.qtd_estoque = int(request.POST.get('qtd_estoque', produto.qtd_estoque))
        
        # Convertendo preco para float, substituindo vírgula por ponto
        preco_str = request.POST.get('preco', produto.preco)
        if preco_str:
            preco_str = preco_str.replace(',', '.')
            produto.preco = float(preco_str)

        
        # Acessos pode ser um campo inteiro também
        produto.acessos = int(request.POST.get('acessos', produto.acessos))

        # Atualiza a imagem se uma nova for enviada
        if request.FILES.get('imagem1'):
            produto.imagem1.delete()
            produto.imagem1 = request.FILES['imagem1']


        if request.FILES.get('imagem2'):
            produto.imagem2.delete()
            produto.imagem2 = request.FILES['imagem2']
        
        if request.FILES.get('imagem3'):
            produto.imagem3.delete()
            produto.imagem3 = request.FILES['imagem3']
        
        if request.FILES.get('imagem4'):
            produto.imagem4.delete()
            produto.imagem4 = request.FILES['imagem4']

        produto.save()
        return redirect('pagina_adm')

    cores = Cor.objects.all().values()
    marcas = Marca.objects.all().values()

    context = {
        'produto': produto,
        'cores': cores,
        'marcas': marcas,
    }

    return render(request, 'atualizar_produtos.html', context)

def add_infor(request):
    return render(request, 'add_infor', context)

def tela_produto(request):
    if request.method == "POST":
        # Obtém ou cria as instâncias de Marca, Modelo e Cor
        modelo_nome = request.POST['modelo']
        cor_nome = request.POST['cor']
        marca_nome = request.POST['marca']

        # Procura a marca, modelo e cor, ou cria novos se não existirem
        marca, created = Marca.objects.get_or_create(nome=marca_nome)
        modelo, created = Modelo.objects.get_or_create(nome=modelo_nome)
        cor, created = Cor.objects.get_or_create(nome=cor_nome)

        produto = Produto(
            modelo=modelo,
            descricao=request.POST['descricao'],
            capacidade1=request.POST['capacidade1'],
            capacidade2=request.POST['capacidade2'],
            capacidade3=request.POST['capacidade3'],
            qtd_estoque=request.POST['qtd_estoque'],
            preco=request.POST['preco'],
            cor=cor,
            marca=marca,
            acessos=0  # O campo de acessos é definido automaticamente como 0
        )

        # Salva as imagens
        if 'imagem' in request.FILES:
            produto.imagem1 = request.FILES['imagem']
        if 'imagem2' in request.FILES:
            produto.imagem2 = request.FILES['imagem2']
        if 'imagem3' in request.FILES:
            produto.imagem3 = request.FILES['imagem3']
        if 'imagem4' in request.FILES:
            produto.imagem4 = request.FILES['imagem4']

        produto.save()
        return redirect("tela_produto")  # Redireciona após salvar

    return render(request, "tela_produto.html")

# Create your views here.
# View de teste da branch de template master
def template(request):
    return render(request, "sobre_nos.html") 
