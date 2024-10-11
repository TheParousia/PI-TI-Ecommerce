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
        produto.descricao = request.POST.get('descricao', produto.descricao)
        produto.preco = request.POST.get('preco', produto.preco)
        produto.imagem = request.POST.get('imagem', produto.imagem)
        produto.save()
        return redirect('pagina_adm')
    return render(request, 'atualizar_produtos.html', {'produto': produto})