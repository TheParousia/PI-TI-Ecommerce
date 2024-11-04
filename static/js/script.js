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
