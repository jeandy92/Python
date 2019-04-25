lista = []
pd = '('
pe = ')'
qtdPd = 0
qtdPe = 0
expressao = str(input('Digite sua expressão:'))
for pos in range(0, len(expressao)):
    lista.append(expressao[pos])
for pos in range(0, len(lista)):
    qtdPe = lista.count(pd)
    qtdPd = lista.count(pe)
if qtdPe == qtdPd:
    print('Expressão válida')
else:
    print('Expressão inválida')
