valores = []
num = 0

num = int(input('Digite um valor: '))
valores.append(num)
while True:
    opcao = str(input('Deseja continuar ?[s/n]'))
    while opcao not in 'sn':
       opcao = str(input('opção inválida, deseja continuar ?[s/n] '))
    if opcao.lower() == 's':
        num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado !!!!')
    else:
        valores.append(num)
    if opcao.lower() == 'n':
        print(f'Você digitou os valores {sorted(valores)}')
        break
