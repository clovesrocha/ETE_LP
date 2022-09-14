# arquivo db.py

import sqlite3

conn = sqlite3.connect("todo-app.db")

def criar_tabela_vagas():
    cursor = conn.cursor()
    conn.execute("""
    create table if not exists vagas (
        id_vagas integer primary key autoincrement,
        titulo_vaga text,
        salario_vaga text,
        nome_empresa text,
        nome_cargo text,
        descricao_vaga text,
        status_vaga integer
    )
    """)

def add_vaga(titulo_vaga, salario_vaga, data_vaga, nome_empresa, nome_cargo, descricao_vaga, status):
    conn.execute("insert into vagas (titulo_vaga, salario_vaga, nome_empresa, nome_cargo, descricao_vaga, status) values (?, 0)", (titulo_vaga, salario_vaga, data_vaga, nome_empresa, nome_cargo, descricao_vaga, status))
    conn.commit()

def remover_vaga(id_vaga):
    conn.execute("delete from vagas where id_vaga= ?", (id_vaga))
    conn.commit()

def concluir_vaga(id_vaga):
    conn.execute("update vagas set status_vaga = 1 where id_vaga = ?", (id_vaga))
    conn.commit()

def get_vagas():
    return conn.execute("select id_vagas, titulo_vaga, salario_vaga from vagas")