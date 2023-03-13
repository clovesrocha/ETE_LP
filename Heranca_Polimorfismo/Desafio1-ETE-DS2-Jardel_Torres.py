# Prof. Cloves Rocha
# Aula Prática: Herança e Polimorfismo
# Polimorfismo - Code 1
# Aluno: jardel torres lima
class Animal():
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    def __str__(self):
        return 'Nome: %s \nPeso: %f' % (self.__nome, self.__peso)

    def __gt__(self, other):
        return self.__peso > other.__peso

    def __add__(self, other):
        return Animal(self.__nome + ', ' + other.__nome,
                      self.__peso + other.__peso)

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
# from Animal import Animal
# class Mamifero(Animal):
# classe = 'Mamifero'

#        def __str__(self):
#                 return super().str__() + 'Mamifero'


class Mamifero(Animal):
    classe = 'Mamifero'

    def __init__(self, nome, peso, qtd_olhos, pelagem, qtd_dentes, dieta,
                 gestacao):
        super().__init__(nome, peso)
        self.qtd_olhos = qtd_olhos
        self.pelagem = pelagem
        self.qtd_dentes = qtd_dentes
        self.dieta = dieta
        self.gestacao = gestacao

    def __str__(self):
        return super().__str__(
        ) + '\nQuantidade de olhos: %d\nPelagem: %s\nQuantidade de dentes: %d\nDieta: %s\nGestação: %d dias' % (
            self.qtd_olhos, self.pelagem, self.qtd_dentes, self.dieta,
            self.gestacao)


class Anfibio(Animal):
    classe = 'Anfibio'

    def __init__(self, nome, peso, qtd_olhos, pelagem, dieta, ovos):
        super().__init__(nome, peso)
        self.qtd_olhos = qtd_olhos
        self.pelagem = pelagem
        self.dieta = dieta
        self.ovos = ovos

    def __str__(self):
        return super().__str__(
        ) + '\nQuantidade de olhos: %d\nPelagem: %s\nDieta: %s\nOvos: %d' % (
            self.qtd_olhos, self.pelagem, self.dieta, self.ovos)


class Ave(Animal):
    classe = 'Ave'

    def __init__(self, nome, peso, qtd_olhos, pelagem, dieta, ovos, tamanho):
        super().__init__(nome, peso)
        self.qtd_olhos = qtd_olhos
        self.pelagem = pelagem
        self.dieta = dieta
        self.ovos = ovos
        self.tamanho = tamanho

    def __str__(self):
        return super().__str__(
        ) + '\nQuantidade de olhos: %d\nPelagem: %s\nDieta: %s\nOvos: %d\nTamanho: %s' % (
            self.qtd_olhos, self.pelagem, self.dieta, self.ovos, self.tamanho)


class Peixe(Animal):
    classe = 'Peixe'

    def __init__(self, nome, peso, qtd_olhos, pelagem, dieta, tamanho, agua):
        super().__init__(nome, peso)
        self.qtd_olhos = qtd_olhos
        self.pelagem = pelagem
        self.dieta = dieta
        self.tamanho = tamanho
        self.agua = agua

    def __str__(self):
        return super().__str__(
        ) + '\nQuantidade de olhos: %d\nPelagem: %s\nDieta: %s\nTamanho: %s\nAgua: %s' % (
            self.qtd_olhos, self.pelagem, self.dieta, self.tamanho, self.agua)


class Reptil(Animal):
    classe = 'Reptil'

    def __init__(self, nome, peso, qtd_olhos, pelagem, dieta, nadador, patas):
        super().__init__(nome, peso)
        self.qtd_olhos = qtd_olhos
        self.pelagem = pelagem
        self.dieta = dieta
        self.nadador = nadador
        self.patas = patas

    def __str__(self):
        return super().__str__(
        ) + '\nQuantidade de olhos: %d\nPelagem: %s\nDieta: %s\nNadador: %s\nPatas: %d' % (
            self.qtd_olhos, self.pelagem, self.dieta, self.nadador, self.patas)


log = Mamifero('leao', 130, 2, 'pelos', 32, 'carnivoro', 270)
log1 = Anfibio('sapo', 2, 2, 'pele', 'carnivoro', 30)
log2 = Ave('pombo', 2, 2, 'penas', 'onivoro', 8, 'pequeno')
log3 = Peixe('tilapia', 5, 2, 'escamas', 'herbivoro', 'medio', 'doce')
log4 = Reptil('cobra', 3, 2, 'escamas', 'carnivoro', 'não', 0)
print(log)
print('\n')
print(log1)
print('\n')
print(log2)
print('\n')
print(log3)
print('\n')
print(log4)
print('\n')
