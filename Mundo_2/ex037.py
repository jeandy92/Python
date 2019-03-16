# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal

num = int(input('Número: '))
print('          ESCOLHA UM OPÇÃO DE CONVERSÃO !              ')
opcao = int(input(' 1 - binário    '
                  ' 2 - octal      '
                  ' 3 - hexadecimal\n'))

if opcao == 1:
    print(bin(num))
elif opcao == 2:
    print(oct(num))
elif opcao == 3:
    print(hex(num))
