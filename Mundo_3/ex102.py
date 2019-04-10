def fatorial(num, show=False):
    """
    Calcula o Fatorial de um numero
    :param num:  O numero a ser calculado
    :param show: Opcional Mostra ou não a memória de calculo
    :return: o valor de fatorial de um número
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
help(fatorial)
print(fatorial(5,show= True))
