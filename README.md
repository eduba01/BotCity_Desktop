# Botcity

Exemplo de automação desktop utilizando o programa "Sicalc" para preencher o formulário e gerar um DARF e salvar como .PDF

##  Bot Desktop
 
### Preparação do ambiente

Valide sempre o seu sistema operacional para baixar e instalar corretamente os itens a seguir:
- Instalar o [Git](https://git-scm.com/downloads);
- Instalar [Python](https://www.python.org/downloads/);
- Instalar [Java](https://www.java.com/pt-BR/download/);
- Instalar o [SDK da BotCity](https://documentation.botcity.dev/pt/getting-started/botcity-studio-sdk/);
- Ter uma IDE (por exemplo: [Visual Studio Code](https://code.visualstudio.com/download) ou [Pycharm](https://www.jetbrains.com/pycharm/download/)).

 Python 3.7 ou superior

### Criando seu Primeiro Projeto
 
https://developers.botcity.dev/getting-started
 
### Para criarmos um projeto, precisamos primeiro instalar o pacote Python do cookiecutter
````python -m pip install --upgrade pip setuptools virtualenv cookiecutter````

### Download de templates

Para criarmos um novo projeto usando o modelo de projeto, vamos invocar o cookiecutter

````python -m cookiecutter https://github.com/botcity-dev/bot-python-template/archive/v2.zip````

- Quando solicitado project_type, escolha a opção "1" para Desktop e pressione [enter];
- Para bot_id, digite "HelloBot" e pressione [enter];

### Criar venv
````python -m venv venv````

### Ativar venv
````venv\Scripts\activate````

### Instalação do requirements.txt
````pip install --upgrade -r requirements.txt````

### Executar uma automação local
````python bot.py````

### Materiais de apoio
Documentação: [Tutoriais.](https://documentation.botcity.dev/pt/tutorials/python-automations/desktop/)

### Documentação da BotCity para seguir orientações
Acesse a [documentação da BotCity](https://documentation.botcity.dev/)  <br> (você pode acompanhar em português ou em inglês, basta escolher o idioma na página).
 
 
Referencias:  https://www.youtube.com/watch?v=XI0fwUyI5qE&t=1107s
 <br>             https://www.youtube.com/watch?v=5hdnWIa4WZo


