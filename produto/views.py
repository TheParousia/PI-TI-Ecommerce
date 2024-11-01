from django.shortcuts import render, redirect, get_object_or_404
from .models import Cor
from django.contrib import messages

def cadastrar_cor(request):
    cores = Cor.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        codigo_hex = request.POST.get('codigo_hex')

        if nome and codigo_hex:
            nova_cor = Cor(nome=nome, codigo_hex=codigo_hex)
            nova_cor.save()  # Salva a nova cor no banco de dados
            messages.success(request, "Cor cadastrada com sucesso!")  # Mensagem de sucesso
            return redirect('atualizar_cor')  # Redireciona para a página de atualização de cor

        messages.error(request, "Por favor, preencha todos os campos.")  # Mensagem de erro

    contexto = {
        "cores": cores
    }

    return render(request, "cadastrar_cor.html", contexto)  # Renderiza a página de cadastro

def atualizar_cor(request):
    cores = Cor.objects.all()  # Busca todas as cores do banco de dados
    return render(request, "atualizar_cor.html", {"cores": cores})  # Renderiza a página de atualização com as cores

def cor_cadastrar_atualizar(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        codigo_hex = request.POST.get("codigo_hex")

        print("id: ", id)

        if id != "-1":
            print("Atualizar")
            
            cor = get_object_or_404(Cor, id=id)

            cor.nome = request.POST.get("nome")
            cor.codigo_hex = request.POST.get("codigo_hex")

            cor.save()
            
        else:
            if nome and codigo_hex:
                nova_cor = Cor(nome=nome, codigo_hex=codigo_hex)
                nova_cor.save()  # Salva a nova cor no banco de dados
                messages.success(request, "Cor cadastrada com sucesso!")  # Mensagem de sucesso

         
    
    return redirect('cadastrar_cor')  # Redireciona para a página de atualização se não for uma requisição POST

def cor_deletar(request, id):  # Obtém a cor selecionada
    cor = get_object_or_404(Cor, id=id)
    cor.delete()
    
    return redirect('cadastrar_cor')  # Redireciona para a página de atualização se não for uma requisição POST
