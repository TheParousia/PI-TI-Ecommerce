from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from produto import models
import os

def pagina1(request):
    return HttpResponse("Olá Mundo")

def pagina2(request):
    return HttpResponse("Bem vindo à minha pagina")

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


def frontend(request):
    return render(request, "frontend.html")