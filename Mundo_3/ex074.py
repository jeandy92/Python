import random

numeros = (
random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
count = 0
menor = 0
maior = 0

for count in range(0, len(numeros)):

    if count == 0:
        menor = numeros[count]
        maior = numeros[count]
    else:
        if numeros[count] > maior:
            maior = numeros[count]
        if numeros[count] < menor:
            menor = numeros[count]
    count = count + 1

print(f'Numeros sorteados{numeros}')
print(f'Maior Numero: {maior}')
print(f'Menor Numero: {menor}')
