count = 1
n = 1
while True:
    n = int(input("Ver a tabuada de qual valor \n:"))
    print('-' * 20)
    if n > 0:
        while count <= 10:
            print(f'{n} x {count} = {n * count} ')
            count = count + 1
    print('-' * 20)
    if n < 0:
        print('Fim')
        break
    count = 1
