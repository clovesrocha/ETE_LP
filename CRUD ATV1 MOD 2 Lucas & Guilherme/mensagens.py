import db

MENU_INICIAL = 0

def exibir_cabecalho():
    QTD = 40
    print ("-" * QTD)
    print ("{:^40}".format("VAGAS"))
    print ("-" * QTD)
    print ("{:^40}".format("Digite 0 para voltar para o menu principal"))
    print ("-" * QTD)

def exibir_vagas():    
    for vagas in db.get_vagas():
        check = u'\u2713' if vagas[5] == 1 else ""
        t = "- [{:>4}] {:<47} {:^3}".format(vagas[0], vagas[1], check)
        print (t)
    print ("-" * 60)

def mostrar_opcao_nova_vaga():
    texto_titulo_vaga = input("Insira o titulo da Vaga => ")
    texto_salario_vaga = input("Insira o salário da vaga => ")
    texto_nome_empresa = input("Insira o nome da empresa => ")
    texto_nome_cargo = input("Insira o nome do cargo => ")
    texto_descricao_vaga = input("Insira a descrição da vaga => ")
    num_status_vaga = input(int("Insira o status da vaga (0-Fechado | 1-Aberto) => "))
    print ("adicionando vaga -> " + str(texto_titulo_vaga))
    if texto_titulo_vaga != str(MENU_INICIAL):
        db.add_vaga(texto_titulo_vaga, texto_salario_vaga, texto_nome_empresa, texto_nome_cargo, texto_descricao_vaga,num_status_vaga)   


def mostrar_opcao_deletar_vaga():
    id_vagas = int(input("Qual vaga quer deletar? digite o código => "))
    print ("Deletando -> " + str(id_vagas))
    if id_vagas != MENU_INICIAL:
        db.remover_vaga(id_vagas)

#Funcionalidades do Projeto:
#1. Listar Todas as Vagas
#2. Cadastrar Vaga
#3. Alterar Vaga
#4. Deletar Vaga

#Objeto, oportunidade de emprego deverá ter no mínimo os seguintes campos:
#1. Título da Vaga (texto)
#2. Salário da Vaga (texto)
#3. Data de Criação (data)
#4. Nome da Empresa (texto)
#5. Nome Cargo (texto)
#6. Descrição da Vaga (texto longo)
#7. Status (aberta ou fechada)