# Projeto Integrador para a 3º Saída do Curso Técnico em Informática
## SENAC Castanhal/PA - Unidade João Gluck Paül



    Rua Pedro Porpino da Silva, nº 2773 - Ianetama - Castanhal
    Castanhal - PA CEP: 68740-000
    (91) 4009-6547 | (91) 4009-6545
    E-mail: cepcst@pa.senac.br
    Horário de funcionamento: De segunda a sexta-feira, das 8:00 às 22:00 horas


### Orientações para os alunos:
1- O uso do pacote django-boostrap-v5 foi descontinuado, NÃO INSTALE ELE NO PROJETO, o template master já carrega o mesmo por meio do link da CDN

2- Tenha o cuidado redobrado para o seu códugo não quebrar quando for usado com o template master

3- TODOS AS NOVAS CONTRIBUIÇÕES DEVERÃO SER FEITAS COM BRANCHS CRIADAS A PARTIR DA BRANCH <b><i>HOMOLOG</i></b>, faça sua branch, aplique os comando das intruções abaixo e envie novamente 

#### Intruções para utilização:

1- Clone o repositório com o comando abaixo:

```
git clone https://github.com/TheParousia/PI-TI-Ecommerce.git
```

> Obs.: O repositório será salvo no diretório onde você executar o comando, recomenda-se salvar no Desktop, para isso, pressione o botão direioto do mouse na área de trabalho e clique na opção "abrir no terminal"

2- Feche o terminal abaerto anteriomente e abra a pasta baixada no Visual Studio Code

3- Inicie o terminal do Visual Studio Code e crie o ambiente virtual:

```powershell
python -m venv venv 
```

4- Em seguida, ative o ambiente virtual com o seguinte comando, o comando pode ser escrito de maneira ágil usando a tecla TAB, para isso escreva somente a inicial da pasta e pressione TAB:
```powershell
.\venv\Scripts\activate
```

5- Instale os pacote qu estçao listados no arquivo <i>requirements.txt</i> executando o comando abaixo:
```powershell
pip install -r requirements.txt
```
<br>
<br>
<br>

### Comando úteis para o desenvolvimento
Para cria um novo app dentro do projeto você deve executar o seguinte comando:
```powershell
python .\manage.py startapp <nome_do_app>
```

Onde o <nome_do_app> é o nome do app que será criado

Para executar o servidor e vizualiar como o projeto estar funcionando execute o seguinte comando:
```powershell
python .\manage.py runserver
```