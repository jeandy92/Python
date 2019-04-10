nome = str(input('Seu Nome: ')).strip()
listnome = nome.split()
nms = ''.join(listnome)

print('Seu nome com todas letras maisculas: {}'.format(nome.upper()))
print('Seu nome com todas letras minusculas: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nms)))
print('Seu primeiro nome possui {} letras'.format(len(listnome[0])))


'''
arq = open('listacarros.txt')
carros = arq.read()
carros.upper()
carros.lower()
carros.replace()
carros.capitalize()
carros.title()#palavra por palavra
carros.strip()#remove espaços inuteis
carros.rstrip()
carros.split()
'-'.join(carros)


esc = input('Escolha um carro:')

if esc in carros:
    print('Existe: {}'.format(esc))
    carros.replace('Gol','gol')
else:
    print('Não Existe: {}'.format(esc))
'''
