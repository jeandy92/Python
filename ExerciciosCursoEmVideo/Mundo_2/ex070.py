vQtdProdutos = vTotalProdutos = vQtdProdutos = vNomeProdutoBarato = vPrecoProdutoBarato = 0
while True:
    vNomeProduto = str(input('Nome do produto: '))
    vPreco = float(input('Preco: R$: '))

    if vPrecoProdutoBarato == 0:
        vNomeProdutoBarato = vNomeProduto
        vPrecoProdutoBarato = vPreco

    if vPreco > 1000:
        vQtdProdutos = vQtdProdutos + 1

    if vPreco < vPrecoProdutoBarato:
        vNomeProdutoBarato = vNomeProduto
        vPrecoProdutoBarato = vPreco

    vTotalProdutos += vPreco

    vOpcao = ' '
    while vOpcao not in 'sn':
        vOpcao = str(input('Quer continuar ? [s/n]')).strip().lower()[0]
    if vOpcao == 'n':
        break
print(f'O total da compra foi de  {vTotalProdutos}')
print(f'Temos {vQtdProdutos} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {vNomeProdutoBarato} que custa R${vPrecoProdutoBarato}')
