import random as r
c = 0
t = 9
num = r.randint(1, 10)
print(num)
print('Pensei em numero de 1 a 10, tente adivinhar !!\n\n')
e = int(input('Escolha um numero de 1 a 10:\n '))
while e != num:
    if t == 5:
        print("Você Perdeu, esgotaram-se as tentativas {} de 10".format(t))
        exit(0)
    else:
        print('\nVocê errou, tente novamente ! \nvoce ainda tem {} tentativas\n '.format(t))
        c += c
        t = t - 1
        e = int(input('Escolha um numero de 1 a 10:\n '))
print('\n Você Venceu !!!\n O número que escolhi: {} seu palpite: {}\n tentativas feitas: {} '.format(num, e, c))

