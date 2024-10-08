from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from .models  import Produto

fs = FileSystemStorage()

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def filtrar_produtos(request):
    produtos = Produto.objects.all()

    marca = request.GET.get('marca')
    modelo = request.GET.get('modelo')
    cor = request.GET.get('cor')
    ordenar_por = request.GET.get('ordenar_por')

    if marca:
        produtos = produtos.filter(marca__icontains=marca)
    if modelo:
        produtos = produtos.filter(modelo__icontains=modelo)
    if cor:
        produtos = produtos.filter(cor__icontains=cor)
    if ordenar_por == 'preco_asc':
        produtos = produtos.order_by('preco')
    elif ordenar_por == 'preco_desc':
        produtos = produtos.order_by('-preco')

    return render(request, 'filtrar_produtos.html', {'produtos': produtos})


def contar_produtos(request):
    total_produtos = Produto.objects.count()
    return render(request, 'produtos/contagem.html', {'total_produtos': total_produtos})