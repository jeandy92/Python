# Exercício 7 - Usando a função filter(),
# encontre os valores que são comuns às duas listas abaixo.
a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]

lst = filter(lambda x: x in a, b)
print(list(lst))
