import os
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage()

from app1 import models

def pagina1(request):
    return HttpResponse("Olá mundo")

def pagina2(request):
    return HttpResponse("Bem vindo ao site do CATATAL 77")

def cartao(request):
    template = loader.get_template("cartao.html")

    contexto = {
        "nome": request.GET.get("nome"),
        "mensagem": request.GET.get("mensagem"),
        "remetente": request.GET.get("remetente"),
    }

    return HttpResponse(template.render(contexto,request))

def formulario(request):
    template = loader.get_template("formulario.html")
    return HttpResponse(template.render())

def front_end(request):
    template = loader.get_template("frontend.html")
    return HttpResponse(template.render())
#----------------------------------------------------------------



def cartao_post(request):
    template = loader.get_template("cartao_post.html")

    contexto = {
        "nome": request.POST.get("nome"),
        "mensagem": request.POST.get("mensagem"),
        "remetente": request.POST.get("remetente"),
    }

    return HttpResponse(template.render(contexto,request))

def formulario_post(request):
   # template = loader.get_template("formulario_post.html")
    if request.method == "POST":
        file_name = fs.save('img.jpg', request.FILES['imagem'])
        url = fs.url(file_name)
        cartao = models.Cartao()
        cartao.nome = request.POST.get("nome")
        cartao.remetente = request.POST.get("remetente")
        cartao.mensagem = request.POST.get("mensagem") 
        cartao.imagem = url

        cartao.save()   

        return redirect("listar_cartao")

    return render(request, "formulario_post.html")

def listar_cartao(request):
    cartoes = models.Cartao.objects.all().values()
    context= {
        "cartoes":cartoes

    }
    template = loader.get_template("listar_cartao.html")
    return HttpResponse(template.render(context, request))

def deletar_produto(request,id):
    #cartao = models.Cartao.objects.get(id=id)
    cartao = get_object_or_404(models.Cartao, id=id)
   
    nome_arquivo = os.path.join(cartao.imagem.url)

    caminho_completo = os.path.join(settings.MEDIA_ROOT, nome_arquivo)
    print(caminho_completo)
    if os.path.exists(caminho_completo):
        os.remove(caminho_completo)
        print("existe")
    else:
        print("nao existe")

                
    cartao.delete()
    return redirect("listar_produto")
    

def produto_cartao(request,id):
    produto = models.Produto.objects.get(id=id)
    context ={
        "produto": produto
    }
    if request.method =="POST":
        produto.nome = request.POST.get("nome")
        produto.remetente = request.POST.get("remetente")
        produto.mensagem = request.POST.get("mensagem")
        produto.save()
        return redirect("listar_produto")
   
    return render(request, "formulario_atualizar.html", context)

