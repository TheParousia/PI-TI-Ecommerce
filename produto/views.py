from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Modelo, Marca, Cor

def pagina_home(request):
    return render(request, 'pagina_home.html')

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
