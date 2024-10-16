from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

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
        produto.modelo = request.POST.get('modelo', produto.modelo)
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

        produto.cor = request.POST.get('cor', produto.cor)
        produto.marca = request.POST.get('marca', produto.marca)
        
        # Acessos pode ser um campo inteiro também
        produto.acessos = int(request.POST.get('acessos', produto.acessos))

        # Atualiza a imagem se uma nova for enviada
        if request.FILES.get('imagem'):
            produto.imagem = request.FILES['imagem']

        produto.save()
        return redirect('pagina_adm')
    
    return render(request, 'atualizar_produtos.html', {'produto': produto})
