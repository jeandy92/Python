
vel = int(input('Velocidade de seu carro: '))
limite = 80
multa = 7.00

if vel > limite:
    ult = vel - limite
    print('Voçê ultrapassou o limite de velocidade em {} Km/h por isso será multado'.format(ult))
    print('O valor da multa é de {} para cada Km/h acima do limite'.format(multa))
    print('O valor da Multa: {} ,valor ultapassado: {} KM/h '.format(((vel-limite)*multa), ult))
