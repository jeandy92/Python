from datetime import datetime

anosdenascimento = [ 1995,1996, 2006, 1980,  2016, 2017,1984]
anoatual = datetime.now().year
maiores = 0
menores = 0

for o in range(0, len(anosdenascimento)):
    idade = anoatual - anosdenascimento[o]
    if idade < 21:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('Menores: {}  Maiores de Idade: {} '.format(menores, maiores))
