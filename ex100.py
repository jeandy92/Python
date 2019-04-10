import random
from time import sleep


def sorteia(lst):
    print("Sorteando 5 valores  da lista:")
    for num in range(0, 5):
        lst.append(random.randint(0, 100))
        sleep(0.2)
        print(lst[num], end=' ')
    print("PRONTO")
    return lst


def somapar(lst):
    soma = 0
    print(f"Somando os valores pares de :")
    for num in range(0, len(lst)):
        print(lst[num], end=' ')
        if lst[num] % 2 == 0:
            soma = soma + lst[num]
    print(f"Temos: {soma} ")


numbers = list()
valores = sorteia(numbers)
somapar(valores)
