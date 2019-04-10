def soma(a, b):
    print(f'{a + b}')
    print(f'Valor de A {a} Valor de B {b}')


def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores{valores} temos {s}")



def contador(*num):
    print(f"Recebi os numeros {num} ao todo são {len(num)} numeros ")
    print("fim")


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


# Progama principal
# valores = [7, 2, 5, 0, 4]
# dobra(valores)

#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)
#
# soma(b=10, a=9)
soma2(5, 2)
soma2(10, 5, 6, 9)
