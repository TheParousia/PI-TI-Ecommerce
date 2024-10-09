
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from produto import models
# from .models import Produto


class Produto():
    id = 1
    modelo = "Poco F6 PRO"
    descricao = "Aparelho excelente, para jogos pesados, com uma bateria de 5.000 mAh, que promete durar um dia inteiro de uso. O smartphone vem com um carregador de 67 W, que consegue carregar completamente a bateria em 51 minutos."
    capacidade = "256GB"
    qtdEstoque = 1
    preco = "2.209"
    cor = "Amarelo" 
    marca = "Xiaomi"

def detalhesProduto(request):
    # Tenta buscar o produto pelo ID ou retorna um erro 404 se não encontrado
    #produto = get_object_or_404(Produto, id=produto_id)
    produto = Produto()
    
    # Dados do produto a serem passados para o template
    context = {
        'produto': produto
    }
    # template = loader.get_template("detalhes.html")
    # Renderiza o template 'produto_detalhes.html' com o contexto do produto
    return render(request, 'produto_detalhes.html', context)

    # return HttpResponse("template.render()")
def add_infor(request):

    return render(request, 'add_infor', context)

    