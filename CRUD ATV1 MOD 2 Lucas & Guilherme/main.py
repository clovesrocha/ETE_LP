# arquivo app.py
# Guilherme Freitas dos Santos - gfs2@etepd.com
# Lucas Vitor Ferreira Santoas - lvfs@etepd.com

import db
import mensagens as msg

def main():
    NOVA_VAGA     = 1
    DELETAR_VAGA = 2
    ATUALIZAR_VAGA  = 3
    LISTAR_VAGA   = 4
    
    while True:
        msg.exibir_cabecalho()
        msg.exibir_vagas()
        try:
            # exibe as opções disponíveis
            opcao = int(input("O que deseja fazer? 1 = Nova vaga, 2 = Deletar vaga, 3 = Atualizar Vaga, 4 = Listar vagas => "))

            # verifica qual opção o usuário escolheu
            if opcao == NOVA_VAGA:
                msg.mostrar_opcao_nova_vaga()
            elif opcao == DELETAR_VAGA:
                msg.mostrar_opcao_deletar_vaga()
            elif opcao == LISTAR_VAGA:
                msg.exibir_vagas()
            else:
                print ("Opção não reconhecida, por favor informar um número")    
        except ValueError as e :
            print ("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.criar_tabela_vagas()

    main()

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