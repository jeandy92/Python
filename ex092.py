from datetime import datetime

now = datetime.now()
funcionario = dict()
anoatual = now.year

nome = str(input("NOME: ")).upper()
while nome == '':
    nome = str(input("NOME: ")).upper()
funcionario['NOME'] = nome

anodenascimento = int(input("ANO DE NASCIMENTO: "))
while anodenascimento >= anoatual or anodenascimento <= 1899:
    print('ANO DE NASCIMENTO INVÁLIDO !!!')
    anodenascimento = int(input("ANO DE NASCIMENTO: "))
funcionario['IDADE'] = anoatual - anodenascimento

cpts = int(input("CARTEIRA DE TRABALHO: "))
while cpts < 0:
    cpts = int(input("CARTEIRA DE TRABALHO (0 NÃO TEM) : "))
funcionario['CPTS'] = cpts

if funcionario['CPTS'] == 0:
    for k, v in funcionario.items():
        if k == 'NOME':
            print(f'Seu nome é {v}')
        if k == 'IDADE':
            print(f'Voce tem {v} anos')
        if k == 'CPTS':
            print('INFELIZMENTE VOCÊ NÃO TEM UM EMPREGO, POR ISSO NÃO PODEMOS CALCULAR SUA APOSENTADORIA')
else:
    anodecontratacao = int(input('ANO DE CONTRATAÇÃO: '))
    while anodecontratacao <= 0 or anodecontratacao >= anoatual:
        print('ANO DE CONTRATAÇÃO INVÁLIDO')
        anodecontratacao = int(input('ANO DE CONTRATAÇÃO: '))
    funcionario['ANODECONTRATACAO'] = anodecontratacao
    funcionario['SALARIO'] = float(input('SALÁRIO: '))

    aposentadoria = anoatual - funcionario['ANODECONTRATACAO']
    funcionario['APOSENTO'] = aposentadoria

    if aposentadoria >= 35:
        print('VOCE PODE SE APOSENTAR')
        print(f'TEMPO DE CONTRIBUIÇÃO MINIMO: 35 SEU TEMPO DE CONTRIBUIÇÃO {aposentadoria}')
        print()
        for k, v in funcionario.items():
            if k == 'NOME':
                print(f'Seu nome: {v}')
            if k == 'IDADE':
                print(f'Voce tem {v} anos')
            if k == 'CPTS':
                print(f'Numero de Registro: {v}')
            if k == 'APOSENTO':
                print(f'Tempo de contribuição:{v} ')
            if k == 'SALARIO':
                print(f'Salário Atual:R${v}')
    else:
        print('VOCE NÃO PODE SE APOSENTAR')
        print(f'TEMPO DE CONTRIBUIÇÃO MINIMO: 35 SEU TEMPO DE CONTRIBUIÇÃO {aposentadoria}')
        for k, v in funcionario.items():
            if k == 'NOME':
                print(f'Seu nome é {v}')
            if k == 'IDADE':
                print(f'Voce tem {v} anos')
            if k == 'CPTS':
                print(f'Numero de Registro{v}')
            if k == 'APOSENTO':
                print(f'Tempo de contribuição:{v}')
            if k == 'SALARIO':
                print(f'Salário Atual:R${v}')
