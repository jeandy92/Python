primo = int(input('Número'))
c = 0
for i in range(1, primo+1):
    if primo %i == 0:
     c = c + 1
    if c == 2:
     print("É primo".format(primo))





