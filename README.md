# 🏋️ FitArena API

Uma API RESTful de alto desempenho para gerenciamento de atletas, categorias e centros de treinamento, construída com FastAPI e SQLAlchemy.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135.1-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-orange?style=flat-square&logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

## 🧐 Sobre o Projeto

O `FitArena API` é um serviço de backend robusto e escalável projetado para gerenciar informações essenciais de um sistema de gerenciamento de academias ou centros de treinamento. Ele fornece uma interface programática para manipular dados de atletas, suas categorias de treinamento e os próprios centros de treinamento.

A arquitetura do projeto é modular, utilizando o framework FastAPI para construir endpoints assíncronos e de alta performance. A persistência de dados é gerenciada por um banco de dados PostgreSQL, com o SQLAlchemy 2.0 atuando como Object-Relational Mapper (ORM) para interações eficientes e seguras com o banco. As migrações de esquema do banco de dados são controladas pelo Alembic, garantindo um versionamento e evolução consistentes do banco.

O design da API segue princípios de uma arquitetura limpa, com a separação clara de responsabilidades entre modelos de dados (SQLAlchemy), esquemas de validação e serialização (Pydantic) e lógica de negócio/controle (controllers). O diretório `fitarena_api/contrib` encapsula componentes reutilizáveis, como modelos base e dependências comuns, promovendo a reusabilidade e a manutenção do código.

## ✨ Funcionalidades

*   **Gerenciamento de Atletas:** Operações CRUD (Criar, Ler, Atualizar, Deletar) para informações de atletas, incluindo associação a categorias e centros de treinamento.
*   **Gerenciamento de Categorias:** Operações CRUD para definir e organizar diferentes categorias de treinamento.
*   **Gerenciamento de Centros de Treinamento:** Operações CRUD para registrar e gerenciar os centros de treinamento disponíveis.
*   **Validação de Dados Robusta:** Utilização do Pydantic para validação automática de requisições e respostas, garantindo a integridade dos dados.
*   **API Assíncrona:** Construída para ser totalmente assíncrona, otimizando o desempenho e a capacidade de resposta.
*   **Documentação Interativa:** Geração automática de documentação OpenAPI (Swagger UI e ReDoc) para fácil exploração e teste dos endpoints.
*   **Migrações de Banco de Dados:** Controle de versão do esquema do banco de dados com Alembic.

## 🛠️ Tecnologias

As seguintes tecnologias foram utilizadas na construção deste projeto:

*   **Python:** Linguagem de programação (versão 3.10+).
*   **FastAPI:** Framework web para construção de APIs RESTful.
*   **SQLAlchemy 2.0:** ORM (Object-Relational Mapper) para interação com o banco de dados, com suporte assíncrono.
*   **Alembic:** Ferramenta de migração de banco de dados para SQLAlchemy.
*   **Pydantic:** Biblioteca para validação de dados e configurações.
*   **Uvicorn:** Servidor ASGI de alta performance para execução da aplicação FastAPI.
*   **PostgreSQL:** Sistema de gerenciamento de banco de dados relacional.
*   **Docker & Docker Compose:** Para orquestração do ambiente de desenvolvimento, especialmente o banco de dados.

## 🚀 Como Começar

Siga estas instruções para configurar e executar o projeto localmente.

### Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em sua máquina:

*   [Python 3.10+](https://www.python.org/downloads/)
*   [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes Python)
*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/tertudev/fitarena-api.git
    cd fitarena-api
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate # No Linux/macOS
    # .venv\Scripts\activate # No Windows
    ```

3.  **Instale as dependências Python:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie o serviço de banco de dados com Docker Compose:**

    ```bash
    docker-compose up -d db
    ```
    Este comando irá iniciar um contêiner PostgreSQL na porta `5432`.

5.  **Execute as migrações do banco de dados:**

    ```bash
    make run-migrations
    ```
    Este comando aplicará todas as migrações pendentes ao seu banco de dados PostgreSQL.

### Execução

Para iniciar a API em modo de desenvolvimento:

```bash
make run
```

A API estará disponível em `http://127.0.0.1:8000`.

Você pode acessar a documentação interativa da API (Swagger UI) em `http://127.0.0.1:8000/docs` e a documentação ReDoc em `http://127.0.0.1:8000/redoc`.

## 📂 Estrutura do Projeto

A estrutura de diretórios do projeto é organizada para promover modularidade e clareza:

```
.
├── alembic/                      # Configurações e scripts de migração do Alembic
├── fitarena_api/                 # Pacote principal da aplicação
│   ├── atleta/                  # Módulo para gerenciamento de atletas
│   │   ├── controller.py         # Lógica de negócio e endpoints para atletas
│   │   ├── models.py             # Modelos SQLAlchemy para atletas
│   │   └── schemas.py            # Schemas Pydantic para validação de dados de atletas
│   ├── categorias/               # Módulo para gerenciamento de categorias
│   │   ├── controller.py         # Lógica de negócio e endpoints para categorias
│   │   ├── models.py             # Modelos SQLAlchemy para categorias
│   │   └── schemas.py            # Schemas Pydantic para validação de dados de categorias
│   ├── centro_treinamento/       # Módulo para gerenciamento de centros de treinamento
│   │   ├── controller.py         # Lógica de negócio e endpoints para centros de treinamento
│   │   ├── models.py             # Modelos SQLAlchemy para centros de treinamento
│   │   └── schemas.py            # Schemas Pydantic para validação de dados de centros de treinamento
│   ├── configs/                  # Configurações da aplicação
│   │   ├── database.py           # Configuração da conexão com o banco de dados
│   │   └── settings.py           # Variáveis de ambiente e configurações gerais
│   ├── contrib/                  # Componentes reutilizáveis e utilitários
│   │   ├── dependencies.py       # Funções de injeção de dependência do FastAPI
│   │   ├── models.py             # Modelos base ou abstratos do SQLAlchemy
│   │   ├── repository/           # Implementação de padrões de repositório (se aplicável)
│   │   └── schemas.py            # Schemas Pydantic base ou comuns
│   ├── main.py                   # Ponto de entrada da aplicação FastAPI
│   └── routers.py                # Agregação e inclusão dos roteadores dos módulos
├── docker-compose.yml            # Definição dos serviços Docker (e.g., PostgreSQL)
├── Makefile                      # Atalhos para comandos comuns (executar, migrar)
├── requirements.txt              # Dependências Python do projeto
└── ...                           # Outros arquivos de configuração e licença
```

## 🤝 Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor, siga os seguintes passos:

1.  Faça um fork do repositório.
2.  Crie uma nova branch para sua feature (`git checkout -b feature/minha-feature`).
3.  Faça suas alterações e commit-as (`git commit -m 'feat: Adiciona minha nova feature'`).
4.  Envie suas alterações para o seu fork (`git push origin feature/minha-feature`).
5.  Abra um Pull Request detalhando suas mudanças.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

Vamos codar o futuro! 🚀
