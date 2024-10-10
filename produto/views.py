from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto  # Assegure-se que o Produto está sendo importado corretamente
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()

def produto(request):
    template = loader.get_template("formulario_post.html")
    contexto = {
        "nome": request.GET.get("nome"),
        "mensagem": request.GET.get("mensagem"),
        "remetente": request.GET.get("remetente"),
    }
    return HttpResponse(template.render(contexto, request))

def formulario(request):
    template = loader.get_template("formulario.html")
    return HttpResponse(template.render())

def clark_post(request):
    template = loader.get_template("clark_post.html")
    contexto = {
        "nome": request.POST.get("nome"),
        "mensagem": request.POST.get("mensagem"),
        "remetente": request.POST.get("remetente"),
    }
    return HttpResponse(template.render(contexto, request))

def formulario_post(request):
    if request.method == "POST":
        produto = Produto()
        produto.nome = request.POST.get("nome")
        produto.remetente = request.POST.get("remetente")
        produto.mensagem = request.POST.get("mensagem")

        if 'imagem' in request.FILES:
            produto.imagem = request.FILES['imagem']

        produto.save()
        return redirect("listar_cartao")

    return render(request, "formulario_post.html")

def listar_cartao(request):
    produtos = Produto.objects.all()  # Corrigido para Produto
    context = {
        "produto": produtos
    }
    return render(request, "listar_cartao.html", context)

def deletar_cartao(request, id):
    produto = get_object_or_404(Produto, id=id)  # Corrigido para Produto
    
    # Remover a imagem do sistema de arquivos se existir
    if produto.imagem:
        if os.path.isfile(produto.imagem.path):
            os.remove(produto.imagem.path)

    # Deletar o cartão do banco de dados
    produto.delete()
    return redirect("listar_cartao")

def atualizar_cartao(request, id):
    produto = get_object_or_404(Produto, id=id)  # Corrigido para Produto

    if request.method == "POST":
        produto.nome = request.POST.get("nome")
        produto.remetente = request.POST.get("remetente")
        produto.mensagem = request.POST.get("mensagem")

        if 'imagem' in request.FILES:
            produto.imagem = request.FILES['imagem']

        produto.save()
        return redirect("listar_cartao")

    context = {
        "produto": produto
    }
    return render(request, "formulario_atualizar.html", context)

def tela_produto(request):
    if request.method == "POST":
        produto = Produto()
        produto.nome = request.POST.get("nome")
        produto.remetente = request.POST.get("remetente")
        produto.mensagem = request.POST.get("mensagem")

        if 'imagem1' in request.FILES:
            produto.imagem = request.FILES['imagem1']
        
        produto.save()   
        return redirect("tela_produto")  # Redireciona após salvar
    return render(request, "tela_produto.html")

def cadastrar_produto(request):
    if request.method == "POST":
        produto = Produto()
        produto.nome = request.POST.get("nome")
        produto.remetente = request.POST.get("remetente")
        produto.mensagem = request.POST.get("mensagem")
        
        if 'imagem' in request.FILES:
            produto.imagem = request.FILES['imagem']
        
        produto.save()
        return redirect("tela_produto")  # Redireciona após salvar
