maior18 = homens = mulheres20 = 0
while True:
    print('=' * 20, 'Cadastro de Pessoas', '=' * 20)
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo[f/m]: ')).lower().strip()
        if idade > 18:
            maior18 = maior18 + 1
        if sexo == 'm':
            homens = homens + 1
        if sexo == 'f' and idade < 20:
            mulheres20 = mulheres20 + 1
    op = ' '
    while op not in 'sn':
        op = str(input("Quer continuar ? [s/n]")).strip().lower()
    if op == 'n':
        break
print(f'Total de pessoas com mais de 18 anos:{maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres20} mulher(s) com menos de 20 anos')
