opcaoSoma = 1
opcaoSubracao = 2
opcaoMultiplicacao = 3
opcaoDivisao = 4
opcaoSaida = 5
cond = True

soma = '1 - Soma'
subtração = '2 - Subtração'
multiplicacao = '3 - Multiplicação'
divisao = '4 - Divisão'
sair = '5 - Sair do Programa'

while True:
    opcao = int(
        input('Escolha uma operação: \n{}\n{}\n{}\n{}\n{}\n'.format(soma, subtração, multiplicacao, divisao, sair)))
    if opcao == opcaoSaida:
        print('Saindo do programa')
        exit(1)
    else:
        num1 = int(input('Primeiro Numero\n'))
        num2 = int(input('Segundo Numero\n'))
        if opcao == opcaoSoma:
            print('Resultado da Soma: {}'.format(num1 + num2))
        else:
            if opcao == opcaoSubracao:
                print('Resultado da Subtração: {}'.format(num1 - num2))
            else:
                if opcao == opcaoMultiplicacao:
                    print('Resultado da Multiplicação: {}'.format(num1 * num2))
                else:
                    if opcao == opcaoDivisao and num2 == 0 and num1 == 0:
                        print('Resultado da Divisão: {}'.format(num1 / num2))
                    else:
                        if opcao == opcaoDivisao and num2 == 0 and num1 != 0:
                            print('Digite um numero diferente de 0')
                        else:
                            if opcao == opcaoDivisao and num2 != 0 and num1 == 0:
                                print('Digite um numero diferente de 0')
                            else:
                                if opcao == opcaoDivisao and num2 != 0 and num1 != 0:
                                    print('Resultado da Divisão: {}'.format(num1 / num2))
