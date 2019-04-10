quadrado = 1
retangulo = 2
triangulo = 3

forma = int(input('1 - Quadrado\n2 - Retâgulo\n3 - Triângulo\n'))

if forma == quadrado:
    h = float(input('Altura: '))
    b = float(input('Base: '))
    area = b ** 2
    litros = area / 2
    print('ÁREA: {} Litros: {}'.format(area, litros))
else:
    if forma == retangulo:
        h = float(input('Altura: '))
        b = float(input('Base: '))
        area = b * h
        litros = area / 2
        print('ÁREA: {} Litros {}'.format(area, litros))
    else:
        if forma == triangulo:
            h = float(input('Altura: '))
            b = float(input('Base: '))
            area = (b * h) / 2
            litros = area / 2
            print('ÁREA: {}, Litros: {}'.format(area, litros))
