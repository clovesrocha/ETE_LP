from Animal import Animal
from Mamifero import Mamifero


# Testes
if __name__ == "__main__":
  animal1 = Animal("Leão", 50)
  print(animal1.peso)

mamifero1 = Mamifero('Lucas', 200, 2)
print(mamifero1.patas)

mamifero1.alimentar(5)
print(mamifero1.peso)

animal1.info()

mamifero1.info()