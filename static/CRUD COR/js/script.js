// static/js/script.js
document.addEventListener('DOMContentLoaded', () => {
    const titulo = document.querySelector("#titulo");
    const btnSalvar = document.querySelector("#btnSalvar");
    const idForm = document.querySelector("#id_da_cor");
    const nomeForm = document.querySelector("#nome");
    const cod_hexForm = document.querySelector("#codigo_hex");
    const btnSelecionarCor = document.querySelector("#btnSelecionarCor");
    const corPalette = document.querySelector("#corPalette");
    const mensagem = document.querySelector("#mensagem");
    const btnAtualizar = document.querySelectorAll(".btnAtualizar");
    const btnCancelar = document.querySelector("#btnCancelar");

    // Exibir seletor de cor e mensagem ao clicar no botão "Selecionar Cor"
    btnSelecionarCor.addEventListener("click", () => {
        corPalette.style.display = "block"; // Mostra o seletor de cor
        cod_hexForm.focus(); // Foca no seletor de cor
        mensagem.style.display = "block"; // Mostra a mensagem
    });

    btnAtualizar.forEach((btn) => {
        btn.addEventListener("click", selecionarCor);
    });

    btnCancelar.addEventListener("click", limparForm);

    function limparForm() {
        idForm.value = "-1";
        nomeForm.value = "";
        cod_hexForm.value = "#000000";
        corPalette.style.display = "none"; // Esconde o seletor de cor
        mensagem.style.display = "none"; // Esconde a mensagem

        // Reseta o título e o botão "Salvar"
        titulo.textContent = "Cadastrar Cor";
        btnSalvar.textContent = "Cadastrar Cor"; // Volta a ser "Cadastrar Cor"
    }

    function selecionarCor(e) {
        const idLinha = e.target.getAttribute("data-id");
        const linha = document.querySelector("#cor" + idLinha);
        const dados = linha.querySelectorAll("td");
        
        idForm.value = dados[0].textContent;
        nomeForm.value = dados[1].textContent;
        const corSelecionada = dados[2].querySelector('.cor-circulo').style.backgroundColor;

        cod_hexForm.value = corSelecionada;

        titulo.textContent = "Atualizar a cor: " + idLinha;
        btnSalvar.textContent = "Atualizar"; // Muda o texto para "Atualizar"
    }
});
