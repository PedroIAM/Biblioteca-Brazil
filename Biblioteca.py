import pandas as pd
import psycopg2
import time
import os
from dotenv import load_dotenv

load_dotenv()

conexao = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
connect = conexao.cursor()
def cadastrar_livro():
    try:
        id_livro = int(input('Me fale o ID do livro?: '))
        nome_livro = input('Qual nome do livro que deseja cadastrar?: ')
        paginas_livro = int(input('Quantas paginas tem o livro?: '))
        autor_livro = input('Qual o autor do livro?: ')
        connect.execute(f"INSERT INTO livros(id_livro,nome_livro,paginas,autor) VALUES ({id_livro},'{nome_livro}',{paginas_livro},'{autor_livro}')")
        conexao.commit()
        print('Livro Cadastrado com Sucesso!!')
    except Exception as erro:
        conexao.rollback()
        print('Erro:', erro)
    input('Tecle ENTER para voltar ao menu')

def cadastrar_cliente():
    try:
        id_livrocomprado = int(input('Me fale o ID do livro?: '))
        nome_cliente = input('Me fale o nome do cliente?: ')
        telefone_cliente = input('Me fale o numero de telefone do cliente?: ')
        nascimento_cliente = input('Me fale o nascimento do cliente?: ')
        status_cliente = input('Qual status desse cliente?: ')
        connect.execute(f"INSERT INTO cliente(livro_comprado,nome_cliente,telefone_cliente,nascimento,status) VALUES ({id_livrocomprado},'{nome_cliente}','{telefone_cliente}','{nascimento_cliente}','{status_cliente}')")
        conexao.commit()
        print('Cliente adicionado com sucesso!')
    except Exception as erro:
        conexao.rollback()
        print('Erro:', erro)
    input('Tecle ENTER para voltar ao menu')

def mostrar_livro():
    try:
        print('Consultando os livros...')
        time.sleep(1)
        livro = pd.read_sql("SELECT nome_livro,autor,paginas FROM livros",conexao)
        print(livro)
    except Exception as erro:
        conexao.rollback()
        print('Erro:', erro)
    input('Tecle ENTER para voltar ao menu')

def mostrar_cliente():
    try:
        print('Consultando clientes...')
        time.sleep(1)
        cliente = pd.read_sql("SELECT nome_cliente,telefone_cliente,nascimento,status FROM cliente",conexao)
        print(cliente)
    except Exception as erro:
        conexao.rollback()
        print('Erro:', erro)
    input('Tecle ENTER para voltar ao menu')

def remover_livro():
    try:
        perg_livro = int(input('Qual o ID do livro que deseja remover?: '))
        connect.execute(f"DELETE FROM livros WHERE id_livro = {perg_livro}")
        if connect.rowcount == 0:
            conexao.rollback()
            print('Livro não encontrado.')
        else:
            conexao.commit()
            print('Livro deletado com sucesso!')
    except Exception as erro:
        conexao.rollback()
        print('Erro:', erro)
    input('Tecle ENTER para voltar ao menu')

def remover_cliente():
    try:
        perg_cliente = str(input('Qual nome do cliente que deseja remover?:'))
        connect.execute(f"DELETE FROM cliente WHERE nome_cliente = '{perg_cliente}'")
        if connect.rowcount == 0:
            conexao.rollback()
            print('Cliente não encontrado.')
        else:
            conexao.commit()
            print('Cliente removido com sucesso!')
    except Exception as erro:
        conexao.rollback()
        print('Erro:', erro)
    input('Tecle ENTER para voltar ao menu')

def alterar_livro():
    try:
        id_livro = int(input('Qual o ID do livro que deseja alterar?: '))
        novo_nome = input('Novo nome do livro: ')
        novas_paginas = int(input('Novo número de páginas: '))
        novo_autor = input('Novo autor: ')

        connect.execute(f"UPDATE livros SET nome_livro = '{novo_nome}', paginas = {novas_paginas}, autor = '{novo_autor}' WHERE id_livro = {id_livro}"

        )

        if connect.rowcount == 0:
            print('Livro não encontrado.')
        else:
            conexao.commit()
            print('Livro alterado com sucesso!')

    except Exception as erro:
        conexao.rollback()
        print('Erro:', erro)

    input('Tecle ENTER para voltar ao menu')

print('Seja Bem Vindo a Biblioteca Brazil!')
while True:
    print('1) Cadastrar um livro')
    print('2) Cadastrar cliente')
    print('3) Mostrar livros')
    print('4) Mostrar clientes')
    print('5) Remover Livro')
    print('6) Remover cliente')
    print('7) Editar livro')
    print('8) Sair')
    try:
        perg = int(input('O que vamos fazer hoje?: '))
    except ValueError:
        print('Digite um número válido!')
        input('Pressione ENTER para voltar ao MENU')
        continue

    if perg == 1:
        cadastrar_livro()
    elif perg == 2:
        cadastrar_cliente()
    elif perg == 3:
        mostrar_livro()
    elif perg == 4:
        mostrar_cliente()
    elif perg == 5:
        remover_livro()
    elif perg == 6:
        remover_cliente()
    elif perg == 7:
        alterar_livro()
    elif perg == 8:
        print('Saindo do sistema...')
        time.sleep(2)
        break
    else:
        print('Não entendi oque deseja!')
        input('Pressione ENTER para voltar ao MENU')