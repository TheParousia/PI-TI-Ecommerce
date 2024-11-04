from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca  # Importa o modelo Marca
from django.contrib import messages

# View para cadastrar uma nova marca
def cadastrar_marca(request):
    marcas = Marca.objects.all()  # Busca todas as marcas no banco de dados

    if request.method == 'POST':
        nome = request.POST.get('nome')  # Pega apenas o nome

        # Verifica se o campo nome foi preenchido corretamente
        if nome:  
            nova_marca = Marca(nome=nome)  # Cria uma nova instância de Marca
            nova_marca.save()  # Salva a nova marca no banco de dados
            messages.success(request, "Marca cadastrada com sucesso!")  # Mensagem de sucesso
            return redirect('cadastrar_marca')  # Redireciona para a página de cadastro de marca

        messages.error(request, "Por favor, preencha todos os campos.")  # Mensagem de erro

    contexto = {
        "marcas": marcas  # Passa todas as marcas para o template
    }

    return render(request, "cadastrar_marca.html", contexto)  # Renderiza a página de cadastro

# View para atualizar a marca (mostra todas as marcas cadastradas)
def atualizar_marca(request):
    marcas = Marca.objects.all()  # Busca todas as marcas do banco de dados
    return render(request, "atualizar_marca.html", {"marcas": marcas})  # Renderiza a página de atualização com as marcas

# View para cadastrar ou atualizar uma marca
def marca_cadastrar_atualizar(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        nome = request.POST.get("nome")  # Apenas verifica o campo nome

        if id and id != "-1":  # Se o id for diferente de -1, significa que é uma atualização
            marca = get_object_or_404(Marca, id=id)  # Busca a marca no banco de dados
            marca.nome = nome  # Atualiza o nome da marca
            marca.save()  # Salva as alterações no banco de dados
            messages.success(request, "Marca atualizada com sucesso!")  # Mensagem de sucesso
        else:
            # Se o id for -1 ou não estiver presente, significa que é um novo cadastro
            if nome:  # Apenas verifica o campo nome
                nova_marca = Marca(nome=nome)  # Cria uma nova instância de Marca
                nova_marca.save()  # Salva a nova marca no banco de dados
                messages.success(request, "Marca cadastrada com sucesso!")  # Mensagem de sucesso
            else:
                messages.error(request, "Por favor, preencha todos os campos.")  # Mensagem de erro

    return redirect('cadastrar_marca')  # Redireciona de volta para a página de cadastro

# View para deletar uma marca
def marca_deletar(request, id):
    marca = get_object_or_404(Marca, id=id)  # Obtém a marca a ser deletada
    marca.delete()  # Deleta a marca
    messages.success(request, "Marca deletada com sucesso!")  # Mensagem de sucesso
    return redirect('cadastrar_marca')  # Redireciona de volta para a página de cadastro de marcas
