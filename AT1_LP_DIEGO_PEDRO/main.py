##ETE PORTO DIGITAL
##DIEGO LIMA DA SILVA (dls@etepd.com)
##PEDRO LUCAS MANSO (plmp@etepd.com)

from os import system
import time
import conexao as conn

db = conn.DB()

system("Limpar")

def create():
    titulo = str(input("Titulo da Vaga: "))
    salario = str(input("Salario da Vaga: "))
    data = str(input("Data da Vaga: "))
    nome = str(input("Nome da Empresa: "))
    cargo = str(input("Nome do cargo: "))
    descricao = str(input("Descrição da Vaga: "))
    status = str(input("Status da Vaga: "))
    if(len(salario) > 0):
        sql = "INSERT INTO sistema(titulo, salario, data, nome, cargo, descricao, status) VALUES (?, ?, ?, ?, ?, ?, ?)"
        parametros = (titulo, salario, data, nome, cargo, descricao, status)
        db.realizar_consulta(sql, parametros)
        print("Cadastrados")

def read():
    sql = "SELECT * FROM sistema"
    result = db.realizar_consulta(sql)
    for data in result:
        print(""" 
            +ID :        {}
            +TITULO :    {}
            +SALARIO :     {}
            +DATA:        {}
            +NOME:        {}
            +CARGO:        {}
            +DESCRICAO:        {}
            +STATUS:        {}""".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))

def update():
    id = int(input("Insira o id: "))
    if (id != 0):
        titulo = str(input("Titulo da Vaga: "))
        salario = str(input("Salario da Vaga: "))
        data = str(input("Data da Vaga: "))
        nome = str(input("Nome da Empresa: "))
        cargo = str(input("Nome do cargo: "))
        descricao = str(input("Descrição da Vaga: "))
        status = str(input("Status da Vaga: "))
        if(len(titulo) > 0):
            sql = "UPDATE sistema SET titulo=?, salario=?, data=?, nome=?, cargo=?, descricao=?, status=?"
            parametros = (id, titulo, salario, data, nome, cargo, descricao, status)
            db.realizar_consulta(sql, parametros)
            print('Vaga Atualizada')

def delete():
    id = int(input("Insira o id: "))
    if(id != 0):
        sql = "DELETE FROM sistema WHERE id=?"
        parametros = (id,)
        db.realizar_consulta(sql,parametros)
        print("Eliminado!")
    else:
        print("Necessário um ID")

def search():
    emprego = str(input('Pesquisar vaga: '))
    if(len(emprego) > 0):
        sql = "SELECT * FROM sistema WHERE name LIKE ?"
        parametros = ('%{}%'.format(emprego),)
        result = db.realizar_consulta(sql,parametros)
        for data in result:
            print(""" 
            +ID :        {}
            +TITULO :    {}
            +SALARIO :     {}
            +DATA:        {}
            +NOME:        {}
            +CARGO:        {}
            +DESCRICAO:        {}
            +STATUS:        {}""".format(data[0],data[1],data[2], data[3], data[4], data[5], data[6], data[7]))

while True:
    print("=========================================")
    print("\tOportunidades de Emprego")
    print("=========================================")
    print("\t[1] Inserir Vaga")
    print("\t[2] Listar Vaga")
    print("\t[3] Alterar Vaga")
    print("\t[4] Deletar Vaga")
    print("\t[5] Buscar Vaga")
    print("\t[6] Sair")
    print("=========================================")

    try:
        opcao = int(input("selecione uma opção: "))
        if(opcao == 1):
            create()
            time.sleep(1)
        elif (opcao == 2):
            read()
            time.sleep(1)
        elif (opcao == 3):
            update()
            time.sleep(1)
        elif (opcao == 4):
            delete()
            time.sleep(1)
        elif (opcao == 5):
            search()

        elif (opcao == 6):
            break
    except:
        print("Selecione uma opção correta.")