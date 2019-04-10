numeros = []
par = []
impar = []
opcao = ''
numero = int(input('Digite um número\n'))
numeros.append(numero)
while True:
    opcao = str(input('Deseja continuar [s/n] ? '))
    while opcao not in 'sn':
       opcao = str(input('opcão inválida Deseja continuar [s/n] ? ')).lower()
    if opcao == 's':
        numero = int(input('Digite um número\n'))
        numeros.append(numero)
    if opcao == 'n':
        break

for pos in range (0, len(numeros)):
    if numeros[pos] % 2 == 0:
        par.append(numeros[pos])
    elif numeros[pos] % 2 == 1:
        impar.append(numeros[pos])
print(f'Sua Lista: {numeros}')
print(f'Números Pares de sua Lista: {par}')
print(f'Números Impares de sua Lista:: {impar}')