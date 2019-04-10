import random
# print('-' * 10, "JOGO PAR OU IMPAR", '-' * 10)
# opcao = int(input('Escolha:\n1 - Par  ou 2 - Impar\n'))
# num = int(input('\nEscolha um número:\n'))

soma = 0
ten = 0
while True:
    print('-' * 10, "JOGO PAR OU IMPAR", '-' * 10)
    opcao = int(input('Escolha:\n1 - Par  ou 2 - Impar\n'))
    maq = random.randint(0, 10)
    if opcao > 2 or opcao < 0:
        print('Opção inválida !!')
        break

    num = int(input('Escolha um número:\n'))
    soma = num + maq

    if opcao == 1:
        if soma % 2 == 0:
            print(f"\n!!!!! VENCEU !!!!")
            print(" !!!!!! PAR !!!!!!")
            print(f"\n Sua escolha: {num}"
                  f"\n   Escolha da máquina: {maq}"
                  f"\n   Resultado final: {soma}\n")
            ten = ten + 1
        if soma % 2 != 0:
            print("\n!!!!! PERDEU !!!!")
            print(" !!!!!! IMPAR !!!!!!")
            print(f"\n Sua escolha: {num}"
                  f"\n   Escolha da máquina: {maq}"
                  f"\n   Resultado final: {soma}"
                  f"\n   Vitórias consecutivas: {ten}\n")
            break
    elif opcao == 2:
        if soma % 2 != 0:
            print(" \n!!!!! VENCEU !!!!")
            print(" !!!!!! IMPAR !!!!!!")
            print(f"\n Sua escolha: {num}"
                  f"\n   Escolha da máquina: {maq}"
                  f"\n   Resultado final: {soma}"
                  f"\n   Números de tentativas: {ten}\n")
            ten = ten + 1
        if soma % 2 == 0:
            print(f"\n!!!!! PERDEU !!!!")
            print(" !!!!!! PAR !!!!!!")
            print(f"\n Sua escolha: {num}"
                  f"\n   Escolha da máquina: {maq}"
                  f"\n   Resultado final: {soma}"
                  f"\n   Vitórias consecutivas: {ten}\n")
            break

