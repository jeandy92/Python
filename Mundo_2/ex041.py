from datetime  import datetime

anodenascimento = int(input('Ano de nascimento: '))
now = datetime.now()
idade = now.year - anodenascimento

if 0 >= idade <= 9:
    print('MIRIN')
elif 9 > idade <= 14:
    print('INFANTIL')
elif 14 > idade <= 19:
    print('JUNIOR')
elif 19 > idade <= 20:
    print('SÉNIOR')
else:
    print('MASTER')

