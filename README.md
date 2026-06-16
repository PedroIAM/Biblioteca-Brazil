# 📚 Biblioteca Brazil

Sistema de gerenciamento de biblioteca via terminal (CLI), desenvolvido em Python com PostgreSQL. Permite cadastrar, consultar, editar e remover livros e clientes, com tratamento de erros e proteção de credenciais via variáveis de ambiente.

## ✨ Funcionalidades

- 📖 Cadastrar livros (ID, nome, número de páginas, autor)
- 👤 Cadastrar clientes (vinculados a um livro, com telefone, nascimento e status)
- 🔍 Listar todos os livros cadastrados
- 🔍 Listar todos os clientes cadastrados
- ✏️ Editar informações de um livro existente
- ❌ Remover livro (com proteção contra exclusão de livros vinculados a clientes)
- ❌ Remover cliente
- 🛡️ Tratamento de erros em todas as operações, evitando que o sistema quebre com entradas inválidas ou falhas no banco

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **PostgreSQL**
- **psycopg2** — conexão e execução de comandos SQL
- **pandas** — exibição formatada dos dados consultados
- **python-dotenv** — gerenciamento seguro de credenciais

## 🗂️ Estrutura do banco de dados

O projeto utiliza duas tabelas principais:

```sql
CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    id_livro INTEGER UNIQUE NOT NULL,
    nome_livro VARCHAR(255) NOT NULL,
    paginas INTEGER,
    autor VARCHAR(255)
);

CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    livro_comprado INTEGER REFERENCES livros(id_livro),
    nome_cliente VARCHAR(255) NOT NULL,
    telefone_cliente VARCHAR(20),
    nascimento DATE,
    status VARCHAR(50)
);
```

> A tabela `cliente` possui uma **foreign key** para `livros`, garantindo integridade referencial: não é possível remover um livro que ainda esteja vinculado a um cliente.

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/PedroIAM/Biblioteca-Brazil.git
cd Biblioteca-Brazil
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```
DB_HOST=localhost
DB_NAME=nome_do_seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

### 5. Crie as tabelas no PostgreSQL

Execute o script SQL da seção [Estrutura do banco de dados](#%EF%B8%8F-estrutura-do-banco-de-dados) no seu banco PostgreSQL.

### 6. Execute o sistema

```bash
python Biblioteca.py
```

## 📋 Exemplo de uso

```
Seja Bem Vindo a Biblioteca Brazil!
1) Cadastrar um livro
2) Cadastrar cliente
3) Mostrar livros
4) Mostrar clientes
5) Remover Livro
6) Remover cliente
7) Editar livro
8) Sair
O que vamos fazer hoje?:
```

## 🔒 Segurança

As credenciais do banco de dados **não** ficam expostas no código-fonte. Elas são carregadas a partir de um arquivo `.env`, que é ignorado pelo Git (veja `.gitignore`), seguindo boas práticas de segurança para aplicações que lidam com bancos de dados.

## 🧠 Aprendizados do projeto

Este projeto foi desenvolvido para praticar:

- Operações **CRUD** completas com PostgreSQL
- Tratamento de exceções em operações de banco de dados (`try/except` + `rollback`)
- Integridade referencial entre tabelas (foreign keys)
- Boas práticas de segurança (variáveis de ambiente)
- Manipulação e exibição de dados com `pandas`

## 📌 Possíveis melhorias futuras

- Substituir queries com f-string por **queries parametrizadas**, prevenindo SQL Injection
- Adicionar testes automatizados
- Criar uma interface gráfica (Tkinter, PyQt) ou Web (Flask/Django)
- Adicionar logging estruturado em vez de `print`

## 👤 Autor

Desenvolvido por **Pedro** — [GitHub](https://github.com/PedroIAM)

---

⭐ Se este projeto te ajudou de alguma forma, considere deixar uma estrela!
