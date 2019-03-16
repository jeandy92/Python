distancia = int(input('Distancia: '))
precocurta = 0.50
precolonga = 0.45

if distancia <= 200:
    print('O valor da passagem: R${}'.format(distancia*precocurta))
else:
    print('O valor da passagem: R${}'.format(distancia*precolonga))

