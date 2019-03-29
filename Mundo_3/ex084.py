pessoas = list()
pessoa = list()
maiorpeso = menorpeso = 0
start = 0
while True:
    if start == 0:
        pessoa.append(str(input('Nome: ')))
        pessoa.append(float(input('Peso: ')))
        pessoas.append(pessoa[:])
        pessoa.clear()

    op = str(input('Deseja Continuar ? [S/N]')).upper()
    while op not in 'SN':
        op = str(input('Deseja Continuar ? [S/N]')).upper()
    if op == 'S':
        pessoa.append(str(input('Nome: ')))
        pessoa.append(float(input('Peso: ')))
        pessoas.append(pessoa[:])
        pessoa.clear()
    if op == 'N':
        break
    start = 1
print('=-' * 30)
print(f'Pessoas cadastradas: {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas')

for p in pessoas:
    if maiorpeso == 0 and menorpeso == 0:
        nomemenorpeso = p[0]
        nomemaiorpeso = p[0]
        maiorpeso = p[1]
        menorpeso = p[1]
    if p[1] > maiorpeso:
        nomemaiorpeso = p[0]
        maiorpeso = p[1]
    if p[1] < menorpeso:
        nomemenorpeso = p[0]
        menorpeso = p[1]
print(f'O maior peso foi de {maiorpeso}Kg, registrados paras as pessoa(s)', end=' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f"{p[0]}", end=' ')
print(f'\nO menor peso foi de {menorpeso}Kg, registrados paras as pessoa(s)', end=' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f" {p[0]} ", end=' ')
