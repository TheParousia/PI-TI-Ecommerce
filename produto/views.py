from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from .models  import Produto
from .models import Marca, Modelo, Cor, Selecao

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


def selecao_view(request):
    if request.method == 'POST':
        marca_ids = request.POST.getlist('marca')
        modelo_ids = request.POST.getlist('modelo')
        cor_ids = request.POST.getlist('cor')

        selecao = Selecao()
        selecao.save()  # Salva a seleção vazia primeiro

        # Adiciona as marcas selecionadas
        for marca_id in marca_ids:
            selecao.marca.add(marca_id)
        for modelo_id in modelo_ids:
            selecao.modelo.add(modelo_id)
        for cor_id in cor_ids:
            selecao.cor.add(cor_id)

        return redirect('sucesso')  # Redireciona para uma página de sucesso

    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()
    cores = Cor.objects.all()

    return render(request, 'veiculos/selecao.html', {
        'marcas': marcas,
        'modelos': modelos,
        'cores': cores
    })