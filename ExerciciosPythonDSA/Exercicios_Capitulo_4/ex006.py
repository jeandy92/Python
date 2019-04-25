# Exercício 6 - Considerando o range de valores abaixo, use a função filter()
# para retornar apenas os valores negativos.
range(-5, 5)

lst = filter(lambda x: x < 0, range(-5, 5))
print(list(lst))
