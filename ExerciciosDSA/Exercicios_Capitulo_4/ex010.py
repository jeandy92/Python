# Exercício 10 - Considere a lista abaixo e retorne apenas os
# elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print([v for k,v in enumerate(lista) if k > 5])

def add(a,b):
    print (a, "+", b, "=", a + b)

add(4,12)
