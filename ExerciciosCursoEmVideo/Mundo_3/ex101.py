def voto(anonascimento):
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - anonascimento
    if idade < 16:
        return f" com {idade} anos: NÃO VOTA "
    if 16 <= idade < 18 or idade > 65:
        return f" com {idade} anos: VOTO OPCIONAL"
    else:
        return f' com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal

anonascimento = int(input("Digite o ano de nascimento:  "))
print(voto(anonascimento))
