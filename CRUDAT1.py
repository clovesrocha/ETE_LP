class Empresa:

 def __init__(self,titulo_vaga, salario_vaga, data_criacao_vaga, nome_empresa , nome_cargo, descricao_vaga , status):
    self.titulo_vaga = titulo_vaga
    self.salario_vaga = salario_vaga
    self.data_criacao_vaga = data_criacao_vaga
    self.nome_empresa = nome_empresa
    self.nome_cargo = nome_cargo 
    self.descricao_vaga = descricao_vaga
    self.status = status 

Accenture = Empresa('TECHRecruiter', '1.400', '11/09','Accenture','TECH Recruiter','Recrutar','fechado')
Avanede = Empresa('Engenheiro de software', '7.000', '08/09' ,'Avanade','DevSenior JAVA', 'Engenheiro de software', 'aberto')
CRDDATA = Empresa('CLT', '1.800', '14/09','CRDDATA','DevJr','Desenvolver sistemas','aberto')

print("\n")
print( 'titulo: ' + Accenture.titulo_vaga + '\n' + 'salario: ' + Accenture.salario_vaga+'\n' + 'Data de Criação: '+  Accenture.data_criacao_vaga+'\n' +'Nome da empresa: ' + Accenture.nome_empresa + '\n' + 'nome do Cargo: ' + Accenture.nome_cargo+ '\n' +'descrição da vaga: '+ Accenture.descricao_vaga +'\n' + 'status da vaga: '+ Accenture.status)
print( 'titulo: ' + Avanede.titulo_vaga + '\n' + 'salario: ' + Avanede.salario_vaga+'\n' + 'Data de Criação: '+  Avanede.data_criacao_vaga+'\n' +'Nome da empresa: ' + Avanede.nome_empresa + '\n' + 'nome do Cargo: ' + Avanede.nome_cargo+ '\n' +'descrição da vaga: '+ Avanede.descricao_vaga +'\n' + 'status da vaga: '+ Avanede.status)
print( 'titulo: ' + CRDDATA.titulo_vaga + '\n' + 'salario: ' + CRDDATA.salario_vaga+'\n' + 'Data de Criação: '+  CRDDATA.data_criacao_vaga+'\n' +'Nome da empresa: ' + CRDDATA.nome_empresa + '\n' + 'nome do Cargo: ' + CRDDATA.nome_cargo+ '\n' +'descrição da vaga: '+ CRDDATA.descricao_vaga +'\n' + 'status da vaga: '+ CRDDATA.status)
