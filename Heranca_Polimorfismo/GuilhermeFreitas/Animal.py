# Prof. Cloves Rocha
# Aula Prática: Herança e Polimorfismo
# Polimorfismo - Code 1

class Animal():
    def __init__(self, nome, peso):
      self.__nome = nome
      self.__peso = peso
    def __str__(self):
        return 'Nome: %s \nPeso: %f' % (self.__nome, self.peso)
    def __gt__(self, other):
        return self.__peso > other.__peso
    def __add__(self, other):
      return Animal(self.__nome + ', ' + other.__nome, self.__peso + other.__peso)
      
    def alimentar(self, comida):
          self.peso += comida

    def info(self):
      pri = '-='*6
      print(f'{pri} Animal {pri}')
      print('Nome: ', self.nome)
      print('Peso: ', self.peso)
      print(f'{pri*2}=-=-=-=-=')
    
    @property
    def nome(self):
      return self.__nome
      
    @nome.setter
    def nome(self, new_name):
      if type(new_name) == type(str()):
        self.__nome = new_name

    @property
    def peso(self):
      return self.__peso
    
    @peso.setter
    def peso(self, new_peso):
      if type(new_peso) == type(int()):
        self.__peso = new_peso
 