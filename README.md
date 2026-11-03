# Calculadora Python com Docker e Docker Compose

## Sobre o projeto

Este projeto consiste em uma calculadora desenvolvida em Python e executada em um ambiente conteinerizado utilizando Docker e Docker Compose.

O objetivo é praticar conceitos fundamentais de conteinerização, como criação de imagens, configuração de containers e gerenciamento de aplicações com Docker Compose.

A calculadora realiza operações matemáticas básicas e possui tratamento de erros para entradas inválidas e divisão por zero.

## Tecnologias utilizadas

- **Python 3.10.12:** desenvolvimento da aplicação.
- **Docker:** criação de imagens e execução da aplicação em containers.
- **Dockerfile:** definição das instruções para construção da imagem.
- **Docker Compose:** configuração e gerenciamento do serviço.

## Estrutura do projeto

```text
python-calculadora-docker-compose/
│
├── calculadora.py
├── Dockerfile
├── docker-compose.yaml
├── .gitignore
└── README.md
```

## Funcionalidades

A calculadora permite realizar as seguintes operações:

- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)

Também possui tratamento de exceções para:
- Valores numéricos inválidos.
- Divisão por zero.
- Operadores não reconhecidos.

## Como executar o projeto

### 1. Pré-requisitos

É necessário ter instalado:

- Docker Desktop ou Docker Engine.
- Docker Compose.

### 2. Construir a imagem Docker

Na raiz do projeto, execute:

```bash
docker build -t imagem-calculadora .
```

### 3. Executar com Docker Compose

Execute o comando:

```bash
docker compose run --rm calculadora
```

O Docker Compose criará um container temporário para executar a calculadora. Após o encerramento da aplicação, o container será removido automaticamente.

## Conceitos praticados

Durante o desenvolvimento, foram praticados conceitos como:

- Criação de imagens Docker.
- Construção e utilização de Dockerfile.
- Configuração de serviços com Docker Compose.
- Execução de containers.
- Utilização de variáveis de configuração do Compose.
- Gerenciamento de containers e imagens.
- Versionamento do código com Git e GitHub.


