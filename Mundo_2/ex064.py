import random
n = 0
soma = 0
i=0
count = 0
while i != 999:
     count = count + 1
     i = random.randint(0, 999)
     # print(i)
     # n = int(input('Numero:'))
     if i != 999:
      soma = (soma + i)
print(f'Soma de todos os numero: {soma}')
print(f'Contagens de quantas vezes o computador executou o randon: {count}')
