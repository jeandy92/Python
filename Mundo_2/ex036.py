# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valordacasa = float(input('Valor da casa: '))
salario = float(input('Sálario do Comprador: '))
qtdanos = int(input('Quantos anos pretende pagar o empréstimo: '))

teto = salario + (salario * 0.30)
prestacao = valordacasa / qtdanos

if prestacao <= teto:
    print('EMPRÉSTIMO APROVADO !!')
    print('Valor da casa: {}'.format(valordacasa))
    print('Valor das parcelas: {}'.format(prestacao))
    print('Teto Parcela: {}'.format(teto))
elif prestacao > teto:
    print('EMPRÉSTIMO REPROVADO !!')
    print('Valor da casa: {}'.format(valordacasa))
    print('Valor das parcelas: {}'.format(prestacao))
    print('Teto Parcela: {}'.format(teto))
