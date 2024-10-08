from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto  # Certifique-se de ter o modelo Produto

def pagina_home(request):
    return render(request, 'pagina_home.html')

def pagina_adm(request):
    produtos = Produto.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'pagina_adm.html', {'produtos': produtos})

def criar_produtos(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        preco = request.POST['preco']
        imagem = request.POST['imagem']
        Produto.objects.create(nome=nome, preco=preco, imagem=imagem)
        return redirect('pagina_adm')  # Redireciona para a lista de produtos
    return render(request, 'criar_produtos.html')

def excluir_produtos(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('pagina_adm')  # Redireciona para a lista de produtos

def atualizar_produtos(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.preco = request.POST['preco']
        produto.imagem = request.POST['imagem']
        produto.save()
        return redirect('pagina_adm')  # Redireciona para a lista de produtos
    return render(request, 'atualizar_produtos.html', {'produto': produto})
