from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from .models  import Cor, Marca, Modelo, Produto
from django.shortcuts import get_object_or_404

fs = FileSystemStorage()


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

# def search(request):
#     query = request.GET.get('q', '').strip()  # Adicionando um valor padrão e removendo espaços
#     resultados = []

#     if query:
#         # Buscando produtos que correspondam à consulta
#         resultados = Produto.objects.filter(
#             models.Q(marca__nome__icontains=query) |
#             models.Q(modelo__nome__icontains=query) |
#             models.Q(cor__nome__icontains=query) |
#             models.Q(descricao__icontains=query)
#         )

#     return render(request, 'search.html', {'resultados': resultados, 'query': query})
# 

# def search(request):
    # query = request.GET.get('q')
    # resultados = Produto.objects.filter(marca__icontains=query) if query else []
    # return render(request, 'search.html', {'resultados': resultados, 'query': query})

def search(request):
    query = request.GET.get('q')  # Obtém o parâmetro 'q' da URL
    if query:
        # Se houver um termo de pesquisa, realiza a busca
        resultados = Produto.objects.filter(marca__nome__icontains=query)
    else:
        # Se não houver termo de pesquisa, define resultados como uma lista vazia
        # E uma mensagem informativa para o usuário
        resultados = []
        mensagem = "Por favor, insira um termo de pesquisa."
    
    return render(request, 'search.html', {
        'resultados': resultados,  # Lista de produtos encontrados
        'query': query,            # O termo de pesquisa usado
        'mensagem': mensagem if not query else None  # Mensagem se não houver termo de pesquisa
    })