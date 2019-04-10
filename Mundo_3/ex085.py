numeros = list()
pares = list()
impares = list()

for p in range(1, 8):
    num = int(input(f'Digite {p}º valor: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 == 1:
        impares.append(num)
    pares.sort()
    impares.sort()
numeros.clear()
numeros.append(pares[:])
numeros.append(impares[:])


print(f'Numeros: {numeros}')
print(f'Pares: {numeros[0]}')
print(f'Impares: {numeros[1]}')
