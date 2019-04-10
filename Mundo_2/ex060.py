n = int(input('Numero:'))
r = n
f = 1
print('Calculando {}! = '.format(n), end='')
while r > 0:
   print('{}'.format(r), end='')
   print(' x ' if r > 1 else ' = ', end='')
   f *= r
   r -= 1
print('{}'.format(f))





# n! = n . (n - 1)!  =  n . (n - 1) . (n - 2)!  =  n . (n - 1) . (n - 2) . (n - 3) . ... . 1!