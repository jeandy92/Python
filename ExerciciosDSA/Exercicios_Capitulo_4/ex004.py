# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e
# outra para elevar ao cubo.
# Aplique as duas funções aos elementos da lista abaixo.
# Obs: as duas funções devem ser aplicadas simultaneamente.
def quadrado(n):
    return n ** 2


def cubo(n):
    return n ** 3


lista = [0, 1, 2, 3, 4]
funcs = [quadrado, cubo]

for i in lista:
    potencia = map(lambda x: x(i), funcs)
    print(list(potencia))
