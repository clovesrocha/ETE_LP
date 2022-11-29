# Prof. Cloves Rocha
# Aula Prática: Herança e Polimorfismo
# Herança - Code 1
class Caneta():
  _estilo = '' #atributo
  _tipo = 20  #atributo
  def escrever(self, msg): #msg = mensagem
      if len(self._estilo + msg) <=
        self._tipo:
          self._estilo += msg
      else:
            print('Não cabe')
  def ler(self):
    return self._estilo

#Herança - Code 2
class Caixa(Caneta):
  def __init__(self, cores):
    self.tipo *= cores
A = Caixa(10)
A._tipo

A.escrever('azul')
A.ler()

