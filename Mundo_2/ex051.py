termo = int(input('Digite o termo:'))
razao = int(input('Digite a razão:'))
count = 0

for i in range(1, termo, razao):
    if count <= 10:
        print(i)
count += count
