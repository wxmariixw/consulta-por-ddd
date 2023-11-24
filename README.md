# Consulta de Cidades por DDD

Este é um serviço que permite aos usuários consultar as cidades associadas a um determinado DDD (código de área). A aplicação é composta por duas partes: um crawler para coletar dados de uma API e enviá-los para um banco de dados PostgreSQL, e uma aplicação web em Python para realizar as consultas.

## Configuração

Antes de executar a aplicação, certifique-se de realizar as seguintes etapas:

1. **Configurar o Crawler:**

   - Navegue até o diretório `crawler`.
   - Configure as informações do banco de dados PostgreSQL e da API de onde os dados serão extraídos
     - Crie um banco de dados no PostgreSQL chamado `grandfinale`
     - Crie um schema chamado `cities`

2. **Executar o Crawler:**

   ```bash
   cd crawler
   python3 crawler.py
   ```

   Isso iniciará o crawler para coletar os dados da API e inseri-los no banco de dados.

3. **Configurar a Aplicação Web:**

   - Navegue até o diretório `web`.
   - Crie um ambiente virtual e instale os `requirements.txt`

4. **Executar a Aplicação Web:**
   ```bash
   cd web
   python app.py
   ```
   Isso iniciará a aplicação web na rota [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Como Usar

1. **Acesse a Aplicação Web:**

   - Abra o navegador e vá para [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **Insira o DDD:**

   - Digite o DDD desejado na caixa de consulta.

3. **Realize a Consulta:**

   - Clique no botão de consulta.

4. **Resultados:**
   - A aplicação exibirá uma lista de cidades associadas ao DDD inserido.

## Observações

- Certifique-se de ter as dependências do Python instaladas. Você pode instalá-las executando `pip install -r requirements.txt` em cada diretório (`crawler` e `web`).

- Este projeto utiliza um banco de dados PostgreSQL. Certifique-se de tê-lo instalado e configurado corretamente.

## Contribuições

[André Luz](https://github.com/andreluz)

[Eduardo Nunes](https://github.com/edununes22)

[Juan Marco Camacho](https://github.com/juanmqc22)

[Mariana Abreu](https://github.com/wxmariixw)

[Miguel Marcondes](https://github.com/miguelmarcondes)
