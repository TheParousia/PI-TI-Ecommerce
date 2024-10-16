from django.shortcuts import render, redirect
from .models import Produto, Marca, Modelo, Cor

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
