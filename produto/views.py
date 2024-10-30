from django.shortcuts import render, redirect
from .models import Cor
from django.contrib import messages

def cadastrar_cor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        codigo_hex = request.POST.get('codigo_hex')

        if nome and codigo_hex:
            nova_cor = Cor(nome=nome, codigo_hex=codigo_hex)
            nova_cor.save()  # Salva a nova cor no banco de dados
            messages.success(request, "Cor cadastrada com sucesso!")  # Mensagem de sucesso
            return redirect('atualizar_cor')  # Redireciona para a página de atualização de cor

        messages.error(request, "Por favor, preencha todos os campos.")  # Mensagem de erro

    return render(request, "cadastrar_cor.html")  # Renderiza a página de cadastro

def atualizar_cor(request):
    cores = Cor.objects.all()  # Busca todas as cores do banco de dados
    return render(request, "atualizar_cor.html", {"cores": cores})  # Renderiza a página de atualização com as cores

def cor_atualizada(request):
    if request.method == 'POST':
        cor_selecionada = request.POST.get('cor')  # Obtém a cor selecionada
        nome_da_cor = Cor.objects.filter(codigo_hex=cor_selecionada).first()  # Busca o nome da cor pelo código
        if nome_da_cor:
            nome_da_cor = nome_da_cor.nome
        else:
            nome_da_cor = "Cor Desconhecida"  # Caso não encontre a cor
        return render(request, "cor_atualizada.html", {"nome_da_cor": nome_da_cor})  # Renderiza a página de confirmação

    return redirect('atualizar_cor')  # Redireciona para a página de atualização se não for uma requisição POST
