altura = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso / (altura * altura)
print(imc)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Peso Ideal')
elif 25 <= imc <= 30:
    print('SobrePeso')
elif 30 <= imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')
