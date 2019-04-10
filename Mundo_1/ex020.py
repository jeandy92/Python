import random as r

cont = 0

nomes = []

while cont <= 3:
    nome = input('Digite um nome: \n')
    nomes.append(nome)
    cont = cont + 1

r.shuffle(nomes)

i = 0
while i <= 3:
    print("{}° a se apresentar : {}".format(i+1, nomes[i]))
    i = i + 1
