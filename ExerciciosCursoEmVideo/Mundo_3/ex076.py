listagem = ('Lápis', 1.75
            , 'Borracha', 2
            , 'Caderno', 15.90
            , 'Estojo', 25
            , 'Transferidor', 4.20
            , 'Compasso', 9.9
            , 'Mochila', 120.32
            , 'Canetas', 22.30
            , 'Livro', 34.90)
produto = ''
print('-'*40)
print(F'{"LISTA ESCOLAR":^40}')
print('-'*40)

for pos in range(0, len(listagem)):

    if pos %2 == 0:
         print(f'{listagem[pos]:.<40}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')


