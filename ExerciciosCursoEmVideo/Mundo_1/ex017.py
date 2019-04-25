import math

co = float(input('Valor do cateto Oposto: '))
ca = float(input('Valor do cateto Adjacente:'))

print('Valor do cateto Oposto: {}\n'
      ',Valor do cateto Adjacente: {}\n'
      ',com base nos catetos a hipotenusa do triãngulo é: {:.2f}'.format(co, ca, (math.hypot(co, ca))))
