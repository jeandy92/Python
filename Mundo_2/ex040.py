nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('!!!!!!REPROVADO!!!!!!')
    print('Sua média {}'.format(media))
elif 5.0 <= media <= 6.9:
    print("!!!!!RECUPERAÇÃO!!!!!")
    print('Sua média {}'.format(media))
elif media >= 7.0:
    print("!!!!!APROVADO!!!!!!!!")
    print('Sua média {}'.format(media))

