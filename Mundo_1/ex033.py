num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo  Número: '))
num3 = int(input('Terceiro Número: '))

if num1 == num2 and num2 == num3:
    print('NUMEROS IGUAIS')
else:
    if num1 >= num2 and num1 >= num3:
        print('Maior: {}'.format(num1))
    else:
        if num2 >= num1 and num2 >= num3:
            print('Maior: {}'.format(num2))
        else:
            if num3 >= num1 and num3 >= num2:
                print('Maior: {}'.format(num3))
