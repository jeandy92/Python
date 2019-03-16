import random as r

num = r.randint(1, 5)
print('Pensei em numero de 1 a 5, tente adivinhar !!\n\n')
e = int(input('Escolha um numero de 1 a 5: '))
if e == num:
    print('\nVocê Venceu !!!\n o numero que escolhi: {} seu palpite: {} '.format(num, e))
else:
    print('\nVocê Perdeu !!!\n o numero que escolhi: {} seu palpite: {} '.format(num, e))
