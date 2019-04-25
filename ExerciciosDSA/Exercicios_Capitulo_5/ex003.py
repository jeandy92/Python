# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e
# crie a classe MP3Player com os
# atributos capacidade.
# A classe MP3player deve herdar os atributos da classe Smartphone.


class Smartphone(object):
    def __init__(self, tamanho, interface):
        print("Smartphone criado")
        self.tamanho = tamanho
        self.interface = interface

    def __str__(self):
        return f"Tamanho:{self.tamanho} - Interface: {self.interface}"


class Mp3Player(Smartphone):
    def __init__(self, capacidade, tamanho="Pequeno", interface='Led'):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)
        print("Objeto criado")

    def print_mp3Player(self):
        print(f"Valores para o objeto criado tamanho {self.tamanho, self.interface, self.capacidade}")


device1 = Mp3Player('64 GB')
device1.print_mp3Player()
