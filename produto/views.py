from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from .models  import Cor, Marca, Modelo, Produto
from django.shortcuts import get_object_or_404

fs = FileSystemStorage()


def produtos(request):
    produtos = Produto.objects.all()

    marca_id = request.GET.get('marca')
    modelo_id = request.GET.get('modelo')
    cor_id = request.GET.get('cor')
    preco_min = request.GET.get('preco_min', 0)
    preco_max = request.GET.get('preco_max', 20000)
    ordenar_por = request.GET.get('ordenar_por')
    
    print("Id da marca: ", marca_id)

    # Filtragem
    if marca_id:
        produtos = produtos.filter(marca=marca_id)
    if modelo_id:
        produtos = produtos.filter(modelo=modelo_id)
    if cor_id:
        produtos = produtos.filter(cor=cor_id) 

    try:
        preco_min = float(preco_min)
        preco_max = float(preco_max)
    except ValueError:
        preco_min, preco_max = 0, 20000  # Valores padrão em caso de erro

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
        'modelos': Modelo.objects.all(),
        'cores': Cor.objects.all(),
        'marca_selecionada': marca_id,
        'modelo_selecionado': modelo_id,
        'cor_selecionada': cor_id,
        'preco_min': preco_min,
        'preco_max': preco_max,
        'ordenar_por': ordenar_por,
    }

    return render(request, 'produtos.html', context)

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.acessos += 1
    produto.save()
    
    return render(request, 'produto_detalhes.html', {'produto': produto})