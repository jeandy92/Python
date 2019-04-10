def leiaInt(parametro=""):
    num = str(input(parametro))
    while not num.isnumeric():
        print("\033[0;31m ERRO NUMERO INVÁLIDO.\033[m")
        num = str(input(parametro))
    return num


# Programa Principal
n = leiaInt("Digite um numero: ")
print(f"Você acabou de digitar o numero {n}")
