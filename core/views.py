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
    return HttpResponse("Bem vindo ao site do CAL")

def produto(request):
    template = loader.get_template("produto.html")

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



def produto_post(request):
    template = loader.get_template("produto_post.html")

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
        produto = models.produto()
        produto.nome = request.POST.get("nome")
        produto.remetente = request.POST.get("remetente")
        produto.mensagem = request.POST.get("mensagem") 
        produto.imagem = url

        produto.save()   

        return redirect("listar_produto")

    return render(request, "formulario_post.html")

def listar_produto(request):
    produtos = models.produto.objects.all().values()
    context= {
        "produtos":produtos

    }
    template = loader.get_template("listar_produto.html")
    return HttpResponse(template.render(context, request))

def deletar_produto(request,id):
    #produto = models.produto.objects.get(id=id)
    produto = get_object_or_404(models.produto, id=id)
   
    nome_arquivo = os.path.join(produto.imagem.url)

    caminho_completo = os.path.join(settings.MEDIA_ROOT, nome_arquivo)
    print(caminho_completo)
    if os.path.exists(caminho_completo):
        os.remove(caminho_completo)
        print("existe")
    else:
        print("nao existe")

                
    produto.delete()
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

