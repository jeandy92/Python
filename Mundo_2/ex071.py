print('=' * 50)
print('BANCO DEV')
print('=' * 50)
valor = int(input('Quanto deseja sacar ? '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

#
#         vNotas50 = valor // 50
#         vNotas20 = (valor - (vNotas50*50)) // 20
#         vNotas10 = ((valor - ((vNotas20*20)+(vNotas50*50))) // 10)
#         vNotas1 = (valor - ((vNotas20*20)+(vNotas50*50)+(vNotas10*10)) // 1)
#
# print(vNotas50)
# print(vNotas20)
# print(vNotas10)
# print(vNotas1)
#
#
#
# vNotas1 = valor // 1
#
#
