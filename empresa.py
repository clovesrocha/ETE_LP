class Empresa:

 def __init__(self,titulo_vaga, salario_vaga, data_criacao_vaga, nome_empresa , nome_cargo, descricao_vaga , status):
    self.titulo_vaga = titulo_vaga
    self.salario_vaga = salario_vaga
    self.data_criacao_vaga = data_criacao_vaga
    self.nome_empresa = nome_empresa
    self.nome_cargo = nome_cargo
    self.descricao_vaga = descricao_vaga
    self.status = status

Pepsi = Empresa('Faxineiro', '1.200', '11/09','Pepsi','faxineiro','faxinar','fechado')
Bradesco = Empresa('Engenheiro de software', '10.000', '08/09' ,'bradesco','DevSenior Python', 'Engenheiro de software', 'aberto')
Santander = Empresa('Gerente', '5.000', '14/09','Santander','gerente geral','Gerenciar a equipe','aberto')

print("\n")
print( 'titulo: ' + Pepsi.titulo_vaga + '\n' + 'salario: ' + Pepsi.salario_vaga+'\n' + 'Data de Criação: '+  Pepsi.data_criacao_vaga+'\n' +'Nome da empresa: ' + Pepsi.nome_empresa + '\n' + 'nome do Cargo: ' + Pepsi.nome_cargo+ '\n' +'descrição da vaga: '+ Pepsi.descricao_vaga +'\n' + 'status da vaga: '+ Pepsi.status)
print( 'titulo: ' + Bradesco.titulo_vaga + '\n' + 'salario: ' + Bradesco.salario_vaga+'\n' + 'Data de Criação: '+  Bradesco.data_criacao_vaga+'\n' +'Nome da empresa: ' + Bradesco.nome_empresa + '\n' + 'nome do Cargo: ' + Bradesco.nome_cargo+ '\n' +'descrição da vaga: '+ Bradesco.descricao_vaga +'\n' + 'status da vaga: '+ Bradesco.status)
print( 'titulo: ' + Santander.titulo_vaga + '\n' + 'salario: ' + Santander.salario_vaga+'\n' + 'Data de Criação: '+  Santander.data_criacao_vaga+'\n' +'Nome da empresa: ' + Santander.nome_empresa + '\n' + 'nome do Cargo: ' + Santander.nome_cargo+ '\n' +'descrição da vaga: '+ Santander.descricao_vaga +'\n' + 'status da vaga: '+ Santander.status)

#victor luiz almeida medeiros / elvis bruno cesario