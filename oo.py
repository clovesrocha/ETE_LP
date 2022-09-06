class Usuario:
 def __init__(self, nome_de_usuario, senha, email):
    self.nome_de_usuario = nome_de_usuario
    self.senha = senha
    self.email = email

gustavo09 = Usuario('gustavo09', '1964', 'gustavo@gmail.com')
print( gustavo09.nome_de_usuario + "\n" + gustavo09.senha + "\n" + "\n" + gustavo09.email)
