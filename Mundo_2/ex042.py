
a = float(input('Valor 1: '))
b = float(input('Valor 2: '))
c = float(input('Valor 3: '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    if a == b == c:
        print('TRIÂNGULO EQUILATERO !!!!')
    if a != b != c != a:
        print('TRIÂNGULO ESCALENO !!!!')
    else:
        print('TRIÂNGULO ISÓCELES !!!!')
else:
    print('NÃO TRIÂNGULO')





