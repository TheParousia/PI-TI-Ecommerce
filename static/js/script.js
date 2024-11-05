document.addEventListener('DOMContentLoaded', () => {
    const titulo = document.querySelector("#titulo");
    const btnSalvar = document.querySelector("#btnSalvar");
    const idForm = document.querySelector("#id_da_marca");
    const nomeForm = document.querySelector("#nome");
    const btnAtualizar = document.querySelectorAll(".btnAtualizar");
    const btnCancelar = document.querySelector("#btnCancelar");

    // Evento para o botão "Cancelar"
    btnCancelar.addEventListener("click", limparForm);

    // Evento para os botões de "Atualizar"
    btnAtualizar.forEach((btn) => {
        btn.addEventListener("click", selecionarMarca);
    });

    // Função para limpar o formulário
    function limparForm() {
        idForm.value = "-1";  // Reseta o ID da marca (indica um novo cadastro)
        nomeForm.value = "";  // Limpa o campo de nome

        // Reseta o título e o botão "Salvar"
        titulo.textContent = "Cadastrar Marca";
        btnSalvar.textContent = "Cadastrar Marca";  // Volta o texto para "Cadastrar"
    }

    // Função para preencher o formulário com os dados da marca selecionada
    function selecionarMarca(e) {
        const idMarca = e.target.getAttribute("data-id");  // Obtém o ID da marca
        const nomeMarca = e.target.getAttribute("data-nome");  // Obtém o nome da marca

        // Preenche os campos do formulário com os dados da marca
        idForm.value = idMarca;  // Preenche o ID no formulário
        nomeForm.value = nomeMarca;  // Preenche o nome no formulário

        // Atualiza o título e o botão "Salvar" para indicar atualização
        titulo.textContent = "Atualizar a marca: " + nomeMarca;
        btnSalvar.textContent = "Atualizar";  // Muda o botão para "Atualizar"
    }
});


function updatePreview() {
    document.getElementById('previewModelo').textContent = "Modelo: " + document.getElementById('modelo').value;
    document.getElementById('previewDescricao').textContent = "Descrição: " + document.getElementById('descricao').value;
    document.getElementById('previewCapacidade').textContent = "Capacidades: " + document.getElementById('capacidade1').value + ", " + document.getElementById('capacidade2').value + ", " + document.getElementById('capacidade3').value;
    document.getElementById('previewEstoque').textContent = "Quantidade no Estoque: " + document.getElementById('estoque').value;
    document.getElementById('previewPreco').textContent = "Preço: " + document.getElementById('preco').value;
    document.getElementById('previewCor').textContent = "Cor: " + document.getElementById('cor').value;
    document.getElementById('previewMarca').textContent = "Marca: " + document.getElementById('marca').value;

    const freteSim = document.getElementById('freteSim').checked;
    const freteNao = document.getElementById('freteNao').checked;
    document.getElementById('previewFrete').textContent = "Frete: " + (freteSim ? "Sim" : (freteNao ? "Não" : ""));

    const devolucaoSim = document.getElementById('devolucaoSim').checked;
    const devolucaoNao = document.getElementById('devolucaoNao').checked;
    document.getElementById('previewDevolucao').textContent = "Devolução: " + (devolucaoSim ? "Sim" : (devolucaoNao ? "Não" : ""));

    // Atualiza as prévias das imagens
    const previews = ['preview1', 'preview2', 'preview3', 'preview4'];
    const previewImagesDiv = document.getElementById('previewImages');
    previewImagesDiv.innerHTML = ''; // Limpa a prévia anterior

    previews.forEach((previewId) => {
        const imageElement = document.getElementById(previewId).querySelector('img');
        if (imageElement) {
            const newImage = document.createElement('img');
            newImage.src = imageElement.src;
            newImage.style.width = '130px'; // Define a largura da imagem
            newImage.style.height = '130px'; // Define a altura da imagem
            newImage.style.objectFit = 'cover'; // Para manter a proporção da imagem
            newImage.style.marginRight = '10px';
            previewImagesDiv.appendChild(newImage);
        }
    });
}

function previewImage(input, previewId) {
    const file = input.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.width = '130px'; // Define a largura da imagem
            img.style.height = '130px'; // Define a altura da imagem
            img.style.objectFit = 'cover'; // Para manter a proporção da imagem
            document.getElementById(previewId).innerHTML = ''; // Limpa a prévia anterior
            document.getElementById(previewId).appendChild(img);
            updatePreview(); // Atualiza a pré-visualização após selecionar uma imagem
        };
        reader.readAsDataURL(file);
    }
}

function validateForm() {
    // Aqui você pode adicionar validações específicas, se necessário
    return true; // Retorne false para impedir o envio do formulário
}
