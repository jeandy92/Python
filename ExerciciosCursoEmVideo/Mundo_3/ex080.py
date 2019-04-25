valores = []
menor = maior = num = 0
for c in range(0, 5):
    num = int(input('Digite um valor:'))
    if c == 0 or num > valores[-1]:
        print('Adicionado ao final da lista...')
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionando na posicão {pos} da Lista')
                break
            pos += 1
print('=0' * 30)
print(f'Ordem: {valores}')