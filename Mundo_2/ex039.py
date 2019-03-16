from datetime  import datetime

anodenascimento = int(input('Ano de nascimento: '))
now = datetime.now()
idade = now.year - anodenascimento

if idade < 18:
    print('Ainda falta {} anos para seu alistamento'.format(18-idade))
elif idade == 18:
    print('Hora de se alistar')
elif idade > 18:
    print('Prazo de alistamento já se encerrou, voce está {} anos fora do prazo'.format(idade-18))
