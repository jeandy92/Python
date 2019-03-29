import random
from time import sleep

print("=-" * 20)
print("JOGA NA MEGA SENA".center(40))
print("=-" * 20)
megasena = list()
jogo = list()
vezes = int(input("Quantos jogos você quer que eu sorteie?\n"))
c = num = 0
i = 0
pos = 1
while c < vezes:
    jogo.clear()
    count = 0
    while True:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            count = count + 1
        if count >= 6:
            break
    megasena.append(jogo[:])

    c = c + 1
while i < len(megasena):
    sleep(1)
    megasena[i].sort()
    print(f"Jogo {pos}: {megasena[i]}")
    i = i + 1
    pos = pos + 1

