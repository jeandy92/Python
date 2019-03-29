extNum = ('zero', 'um', 'dois','tres', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

num = int(input('Digite um número entre 0  e 20:'))
while num < 0 or num > 20:
    num = int(input('Tente Novamente. Digite um Numero entre 0 e 20:'))

print(f'Você digitou o numero {extNum[num]}')
