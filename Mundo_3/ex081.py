numeros = []
opcao = ''
existe = False
posicao = []
vezes = 0
while True:
    numero = int(input('Digite um número\n'))
    numeros.append(numero)
    opcao = str(input('Deseja continuar ?\n')).lower()
    if opcao == 'n':
        for pos in (0, len(numeros)):
            if numeros.count(5) > 0:
                existe = True
                posicao.append(pos)
                vezes = numeros.count(5)
        break
numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} elementos ')
print(f'Os valores decrescente são {numeros}')
if existe:
    print(f'O valor 5 faz parte da Lista, aparece: {vezes} vezesnas posições {posicao}')
else:
    print(f'O valor 5 não faz parte da Lista {numeros}')
