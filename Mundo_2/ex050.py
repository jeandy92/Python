s = 0
n = 0
pares = []
impares = []
for i in range(0, 7):
    n = int(input('DIGITE UM NÚMERO:'))
    if n % 2 == 0:
        s += n
        pares.append(n)
    else:
        impares.append(n)

print("\nPares   = {} ".format(pares))
print("Impares = {} ".format(impares))
print('Soma    = {} '.format(s))