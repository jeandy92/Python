num_1 = int(input('Digite um numero: '))
num_2 = int(input('Digite um numero: '))
num_3 = int(input('Digite um numero: '))
num_4 = int(input('Digite um numero: '))

numeros = (num_1, num_2, num_3, num_4)
pares = ()
count = 0
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 aparece {numeros.count(9)} vezes')
if numeros.count(3) != 0:
    print(f'O valor 3 aparece {numeros.index(3)} posição')
else:
    print(f'O valor 3 não foi encontrado !!')
print(f'Os valores pares são: ', end='')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')

#
# for count in range(0, len(numeros)):
#     if numeros[count] %2 == 0:
