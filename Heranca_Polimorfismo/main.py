# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/vitoriafelix-22/13876ba7e31d1c124a456941bade7d9d/main.ipynb
"""



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
        
        @property
        def nome(self):
                return self.__nome
        @nome.setter
        def nome(self, new_name):
                  if type(new_name) == type(str()):
                          self.__nome = new_name

# Polimorfismo - Code 2 desenvolva o restante no desafio...
from main import Animal
class Mamifero(Animal): 
    def __init__(self, pelos, glandulas_mamarias, vertebrado, carnivoro):
        self.__nome = pelos
        self.__glandulas = glandulas_mamarias
        self.__vertebrado = vertebrado
        self.__carnivoro = carnivoro
        def __str__(self):  
        # return 'Pelos: %s \nGrandulas Mamarias %s \nVertebrado: %s \nCarnivoro: %s Peso: %f ' (self.__carnivoro, self.__pelos, self.__glandulas_mamarias, self.__vertebrado)
        class Repteis(Animal):
    def __init__(self, glandulas, escamas, placas_osseas):
        self.__glandulas = glandulas
        self.__escamas = escamas
        self.__placas_osseas= placas_osseas
        def __str__(self):  
      return 'glandulas: %s \nPlacas_osseas: %s \nEscamas:' (self.__glandulas, self.__Placas_osseas, self.__Escamas)

class Reptil(Animal):
    def __init__(self, nome, peso, tipo_pele):
        super().__init__(nome, peso)
        self.tipo_pele = tipo_pele

    def rastejar(self):
        print('Rastejando...')

    def __str__(self):
        return super().__str__() + '\nEspecie: ' + self.especie + '\nTipo de pele: ' + self.tipo_pele

        class Peixe(Animal):
    def __init__(self, nome, peso, tipo_agua):
        super().__init__(nome, peso)
        self.tipo_agua = tipo_agua

    def nadar(self):
        print('Nadando...')

    def __str__(self):
        return super().__str__() + '\nEspecie: ' + self.especie + '\nTipo de água: ' + self.tipo_agua

        class Ave(Animal):
    def __init__(self, nome, peso, envergadura):
        super().__init__(nome, peso)
        self.envergadura = envergadura

    def voar(self):
        print('Voando...')

    def __str__(self):
        return super().__str__() + '\nEspecie: ' + self.especie + '\nEnvergadura: ' + str(self.envergadura)

        class Anfibio(Animal):
    def __init__(self, nome, peso, tipo_pele):
        super().__init__(nome, peso)
        self.tipo_pele = tipo_pele

    def nadar(self):
        print('Nadando...')

    def pular(self):
        print('Pulando...')

    def __str__(self):
        return super().__str__() + '\nEspecie: ' + self.especie + '\nTipo de pele: ' + self.tipo_pele





