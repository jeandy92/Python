valores = []
posicaomaior = []
posicaomenor = []
menor = maior = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] < menor:
            menor = valores[c]

        if valores[c] > maior:
            maior = valores[c]
print('=-' * 30)
print(f'VOCE DIGITOU OS VALORES:{valores}')
print(f'O MAIOR VALOR: {maior} NA POSIÇÃO', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f' {i}...', end='')
print(f'O MENOR VALOR:{maior} NA POSIÇÃO', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i}...', end='')
print()
