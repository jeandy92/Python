while True:
    print(10*'¨', "MENU", 10*'¨')
    print('| [ 1 ] - SOMAR          |')
    print('| [ 2 ] - MULTI          |')
    print('| [ 3 ] - MAIOR          |')
    print('| { 4 ] - NOVOS NUMEROS  |')
    print('| [ 5 ] - SAIR           |')
    print('|_______________________ |')
    opcao = int(input(':'))
    if opcao == 1:
        print("SOMA !")
        num1 = int(input("Digite um nmero: "))
        num2 = int(input("Digite um nmero: "))
        print("Resultado:\n {} + {} = {} ".format(num1, num2, num1+num2))
    if opcao == 2:
        print("Multiplicação !")
        num1 = int(input("Digite um nmero: "))
        num2 = int(input("Digite um nmero: "))
        print("Resultado:\n {} x {} = {} ".format(num1, num2, num1 * num2))
    if opcao == 3:
        print("MAIOR !")
        num1 = int(input("Digite um nmero: "))
        num2 = int(input("Digite um nmero: "))
        if num1 > num2:
          print("Resultado:\n {} > {} ".format(num1, num2))
        else:
          print("{} < {} ".format(num1, num2))
    if opcao == 4:
        num1 = int(input("Digite um nmero: "))
        num2 = int(input("Digite um nmero: "))
    if opcao == 5:
        exit(0)


