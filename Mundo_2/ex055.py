pesos = [65.3, 62.6, 90, 88, 77, 32, 58, 120, 154]
aux = []
maior = 0
menor = 0

for i in range(0, len(pesos)):
    if i == 0:
        maior = pesos[i]
        menor = pesos[i]
    else:
        if pesos[i] > maior:
            print('Comparação Maior:')
            print(pesos[i], ' > ', maior)
            print('Maior', maior, '\n')
            maior = pesos[i]

        if pesos[i] < menor != 0:
            print('Comparação Menor')
            print(pesos[i], ' < ', menor)
            print('Menor', menor, '\n')
            menor = pesos[i]

print('O Maior peso identificado: {}\nO Menor peso identificado: {}'.format(maior, menor))
