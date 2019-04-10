frase = str(input('Digite uma frase: \n')).strip().lower().split()
fraseSemEspaco = ''.join(frase)

print('Frase:{} Frase Ivertida: {}'.format(fraseSemEspaco, fraseSemEspaco[::-1]))
if fraseSemEspaco == fraseSemEspaco[::-1]:
    print("Palidromo:")
else:
    print("Não palindromo:")
