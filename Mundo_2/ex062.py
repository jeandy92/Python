primeiro = int(input('Digite o termo:'))
razao = int(input('Digite a razão:'))
termo = primeiro
mais = 10
count = 1
n = 0

while mais != 0:
    n = n + mais
    while count <= n:
        print('{}'.format(termo), end='')
        print('-> ' if count < n else '', end='')
        termo += razao
        count += 1
    mais = int(input('\nQuantos termos ?\n:'))
print('Fim !!')
exit(1)

    # if count == n:
    #   r = str(input('\nDeseja mais termos (s/n)?\n:')).upper()
    # elif r == 'S':
    #     n = int(input('Quantos termos ?\n:'))
    # elif r == 'N':
    #    print('Fim !!')
    #    exit(1)
    # elif r != 'S' != 'N':
    #    print('opção inválida !!')
    #    exit(0)
