primeiro = int(input('Digite o termo:'))
razao = int(input('Digite a razão:'))
count = 0
termo = primeiro

while count <= 10:
        print('{} -> '.format(termo), end='')
        termo += razao
        count += 1
