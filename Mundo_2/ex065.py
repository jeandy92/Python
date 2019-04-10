n = 0
media = 0
maior = 0
menor = 0
count = 0
n = int(input('numero: '))
while count >= 0:
    if count >= 0:
        r = str(input('Quer continuar(s/n)? ')).lower()
        if r == 's':
           n = int(input('numero: '))
        elif r == 'n':
            print("Maior: {} ".format(maior))
            print("Menor: {} ".format(menor))
            print("Media: {} ".format(media))
    if count == 0:
       maior = menor = media = n
    if n > maior:
      maior = n
    elif n < menor:
      menor = n
      count = count + 1
      media = (n + media) / count

