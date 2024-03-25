# Projeto Traduzo

O Traduzo é um projeto de uma ferramenta de tradução de textos entre vários idiomas. Ele é desenvolvido utilizando Flask, um microframework para aplicações web em Python, e MongoDB, um banco de dados NoSQL orientado a documentos.

## Tecnologias Principais

- **Flask (Python)**: Um microframework leve que facilita a criação de aplicações web.
- **MongoDB**: Um banco de dados NoSQL que armazena dados em formato de documentos semelhantes a JSON.

## Requisitos e Funcionalidades

- Conexão com o MongoDB.
- Instanciando idiomas.
- Tradução de Textos.
- Listagem de Idiomas.
- Histórico de Traduções.
- Exclusão de Histórico.

## Como Rodar o Projeto

### Preparando o Ambiente

```bash
# Crie um ambiente virtual para o projeto
python3 -m venv venv

# Ative o ambiente virtual
source venv/bin/activate

# Instale as dependências do projeto
python3 -m pip install -r requirements.txt
```

### Iniciando o Projeto
```bash
# Suba o banco de dados MongoDB localmente
mongod --config /usr/local/etc/mongod.conf

# Ou utilize Docker para subir o MongoDB
docker-compose up -d mongodb

# Inicie a aplicação Flask
python3 -u src/app.py

# Ou inicie todo o projeto via Docker
docker-compose up -d
```

### Seeders

```bash
# Execute os seeders para popular o banco de dados com dados necessários para a aplicação funcionar corretamente
python3 -u src/run_seeds.py
```

### Executando os Testes

```bash
# Necessario instalacão das dependências de dev
python3 -m pip install -r dev-requirements.txt

# Utilize o Pytest para executar os testes automatizados do projeto
python3 -m pytest
```
