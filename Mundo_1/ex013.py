preco = float(input('Digite o preço do produto: '))
desconto = 0.05
precod = preco - (preco * desconto)

print('Preco anterior: {}'.format(preco))
print('Valor do desconto: {}'.format(preco * desconto))
print('Preco com desconto: {}'.format(precod))
