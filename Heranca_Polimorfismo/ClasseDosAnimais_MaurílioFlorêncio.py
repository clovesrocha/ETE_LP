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
       
from main import Animal


class Mamifero(Animal):
    def __init__(self,nome, peso, pelo):
        super().__init__(nome, peso)
        self.tipo_pele = pelo
        self.caracteristica_pele = "macia"

    def pelo(self):
        return "O animal possui pele macia com pelo."

    def faz_som(self):
        return "Este mamífero emite sons variados."

class Reptil(Animal):
    def __init__(self,nome, peso, escama):
        super().__init__(nome, peso)
        self.tipo_pele = escama
        self.caracteristica_pele = "grossa"

    def escama(self):
        return "O animal possui escama grossa."

    def faz_som(self):
        return "Este reptil emite um som caracteristico."

class Anfibio(Animal):
    def __init__(self,nome, peso, pele):
        super().__init__(nome, peso)
        self.tipo_pele = pele
        self.caracteristica_pele = "umida"

    def pele(self):
        return "O animal possui pele umida."

    def faz_som(self):
        return "Este anfibio emite um som caracteristico."

class Aves(Animal):
    def __init__(self,nome, peso, pena):
        super().__init__(nome, peso)
        self.tipo_pele = pena
        self.caracteristica_pele = "comum"

    def pena(self):
        return "O animal possui pena comum."

    def faz_som(self):
        return "Esta ave emite um canto melodico."

class Peixes(Animal):
    def __init__(self,nome, peso, escama):
        super().__init__(nome, peso)
        self.tipo_pele = escama
        self.caracteristica_pele = "brilhante"

    def escama(self):
        return "O animal possui escama brilhante."

    def faz_som(self):
        return "Este peixe não emite som."
