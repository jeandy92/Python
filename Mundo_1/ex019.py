import random

cont = 0
nomes = []

while cont <= 3:
    nome = input('Digite um nome:')
    nomes.append(nome)
    cont = cont + 1


print('O nome do escolhio: {}'.format(random.choice(nomes)))
