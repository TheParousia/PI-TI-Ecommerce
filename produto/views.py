from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from produto import models
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()



def clark(request):
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
        clark = models.clark()
        clark.nome = request.POST.get("nome")
        clark.remetente = request.POST.get("remetente")
        clark.mensagem = request.POST.get("mensagem")

        if 'imagem' in request.FILES:
            clark.imagem = request.FILES['imagem']

        clark.save()
        return redirect("listar_cartao")

    return render(request, "formulario_post.html")

def listar_cartao(request):
    clark = models.clark.objects.all()
    context = {
        "clark": clark
    }
    return render(request, "listar_cartao.html", context)

def deletar_cartao(request, id):
    clark = get_object_or_404(models.clark, id=id)
    
    # Remover a imagem do sistema de arquivos se existir
    if clark.imagem:
        if os.path.isfile(clark.imagem.path):
            os.remove(clark.imagem.path)

    # Deletar o cartão do banco de dados
    clark.delete()

    return redirect("listar_cartao")

def atualizar_cartao(request, id):
    clark = get_object_or_404(models.clark, id=id)

    if request.method == "POST":
        clark.nome = request.POST.get("nome")
        clark.remetente = request.POST.get("remetente")
        clark.mensagem = request.POST.get("mensagem")

        if 'imagem' in request.FILES:
            clark.imagem = request.FILES['imagem']

        clark.save()
        return redirect("listar_cartao")

    context = {
        "clark": clark
    }

    return render(request, "formulario_atualizar.html", context)


def tela_produto(request):
    return render(request, "tela_produto.html")


def cadastrar_produto(request):
    if request.method == "POST":
        file_name = fs.save('img.jpg', request.FILES['imagem'])
        url = fs.url(file_name)
        produto = models.Produto()
        produto.nome = request.POST.get("nome")
        produto.remetente = request.POST.get("remetente")
        produto.mensagem = request.POST.get("mensagem") 
        produto.imagem = url

        produto.save()   

        return redirect("tela_produto")

    return render(request, "cadastrar_produto.html")
    #return render(request, "cadastrar_produto.html")
