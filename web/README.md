# Aplicação Web

## Índice
- Tecnologias Utilizadas
  - Linguagens
  - Framework
- Instalação
- Como Rodar a Aplicação

## Linguagens e ferramentas utilizadas

### Linguagem

- Python
- HTML
- CSS
- Javascript

### Framework
- Flask

### Bibliotecas

- Pandas
- SQLalchemy
- pydantic
- JSON

### Banco de dados

- PostgreSQL

## Instalação
### Preparando o ambiente virutal

<details>
  <summary>Windows</summary>
  <ol>
    <li>
      <p>Crie o ambiente vitual</p>
      <code style="white-space:nowrap;">python3 -m venv venv</code>
    </li>
    <li>
      <p>Ative o ambiente virtual</p>
      <code style="white-space:nowrap;">venv\Scripts\activate.bat</code>
    </li>
  </ol>
</details>

<details>
  <summary>Linux</summary>
  <ol>
    <li>
      <p>Crie o ambiente vitual</p>
      <code style="white-space:nowrap;">virtualenv venv</code>
    </li>
    <li>
      <p>Ative o ambiente virtual</p>
      <code style="white-space:nowrap;">cd venv</code>
      <p></p>
      <code style="white-space:nowrap;">source bin/activate</code>
    </li>
  </ol>
</details>

**Instale os requisitos**

```
pip install -r requirements.txt
```

**Caso realize alguma alteração sempre anote no requirements**

```
pip freeze > requirements.txt
```

## Como Rodar a Aplicação

- Para rodar o app, rode o seguinte comando no terminal

```
python3 app.py
```