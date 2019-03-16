n = int(input('Digite um numero: '))
print('-' * 10, 'TABUADA', '-' * 10)
for i in range(0, 10):
    print('   {}  x  {}  =  {}  '.format(n, i, (i * i)))
