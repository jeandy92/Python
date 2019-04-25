
#
# num[2] = 3
# num.append(7)
# num.sort(reverse= True)
# num.insert(2,2)
# if 4 in num:
#     num.remove(4)
# else:
# print(num)
# num.remove(4)
# print (num)
# print(f'Essa lista tem {len(num)} elementos')
#
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor{v}!')
print('CHEGUEI AO FINAL DA LISTA')

a = [ 2, 3,4,7]
b = a #LIGACAO
B = a[:]#cópía

print(f'Lista A: {a}')
print(f'Lista B: {b}')