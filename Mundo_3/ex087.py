matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = list()
par = soma = somacol = coli = maior = 0
col = list()
maiores = list()
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))

        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
            par = matriz[l][c]
            soma = par + soma
        if c == 2:
            col.append(matriz[l][c])
            coli = matriz[l][c]
            somacol = somacol + coli
        if l == 1 and maior == 0:
            maior = matriz[l][c]
            maiores.append(matriz[l][c])
        if l == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]
            maiores.append(matriz[l][c])


for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]:^5}  ]', end=' ')
    print()
print(f"\nPares: {soma},\n Pares mapeados {pares}")
print(f"\nSoma da terceira coluna: {somacol},\n Colunas mapeadas: {col}")
print(f"\nO Maior Número da Segunda Linha {maior},\n Linha mapeada: {maiores}")

