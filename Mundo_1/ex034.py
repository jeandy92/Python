salario = 3662.42
base = 1250.00
aumento10 = 0.10
aumento15 = 0.15

if salario > base:
    aumento = salario * aumento10
    salario = salario + aumento
    print('Novo Salário: {:.2f}'.format(salario))
else:
    if salario <= base:
        aumento = salario * aumento15
        salario = salario + aumento
        print('Novo Sálário: {:.2f}'.format(salario))
    else:
        print('Não tem aumento !! ')
