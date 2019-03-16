#bissexto
#Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
#Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
#Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.

ano = int(input('Ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano normal')
