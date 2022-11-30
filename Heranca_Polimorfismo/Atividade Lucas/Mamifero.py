# Prof. Cloves Rocha
# Aula Prática: Herança e Polimorfismo
# Polimorfismo - Code 2

from Animal import Animal


class Mamifero(Animal):
  def __init__(self, nome, peso, patas):
    super().__init__(nome, peso)
    self.__patas = patas
    
  def __str__(self):
    return super().str__() + 'Mamifero'

  def __add__(self, other):
    return self.__peso > other.__peso

  def alimentar(self, comida):
    self.peso += comida

  def info(self):
    pri = '-='*6
    print(f'{pri} Mamífero {pri}')
    print('Nome: ', self.nome)
    print('Peso: ', self.peso)
    print('Patas: ', self.patas)
    print(f'{pri*2}-=-=-=-=-=')

# Métodos "iguais", porém são instanciados pela subclasse, com a especificação da subclasse
  @property
  def patas(self):
    return self.__patas
  
  @patas.setter
  def patas(self, new_patas):
    if type(new_patas) == type(int()):
      self.__patas = new_patas