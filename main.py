#ETEPD 
#DISCIPLINA: LP
#PROF: CLOVES ROCHA
#ALUNOS: Paulo Renato Pereira Bezerra / Thiago Felipe  Chaves do Nascimento
#email: prpb@etepd.com / tfcdn@etepd.com

import sqlite3

#Criando o banco de dados e conectando ao banco criado
banco = sqlite3.connect('banco_talentos.db')

#Criando um cursor para operar com o banco de dados
cursor = banco.cursor()

#Criando uma tabela com parametros solicitados
cursor.execute("CREATE TABLE joblist (vaga integer, salario float, criado text, empresa text, cargo text, descricao text, status text)")

class JobList:
    def __init__(self, vaga, salario, criado, empresa, cargo, descricao, status):
        self.vaga = vaga
        self.salario = salario
        self.criado = criado
        self.empresa = empresa
        self.cargo = cargo
        self.descricao = descricao
        self.status = status

def ListarVagas():
  
  cursor.execute("SELECT * FROM joblist")
  print(cursor.fetchall())

def CadastrarVagas():
  cursor.execute("INSERT INTO joblist VALUES('Assistente Administrativo',2000,'14/09/2022','SEMOG','Analista Administrativo','Assistente administrativo, com experiência em área financeira (ênfase em negociação bancária)','aberta')")


def AlterarVagas():

def DeletarVagas():