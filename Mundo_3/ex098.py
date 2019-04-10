from time import sleep


def line():
    print("-=" * 20)


def contador(start, stop, step):
    line()
    if start < stop:
        print(f"Contagem de {start} até {stop} de {step} em {step} ")
        for num in range(start, stop + 1, step):
            sleep(0.1)
            print(num, end=' ')
    if start > stop:
        if step == 0:
            step = 1
        if step < 0:
            step *= -1
        print(f"Contagem de {start} até {stop} de {step} em {step}")
        for num in range(start, stop - 1, - step):
            sleep(0.1)
            print(num, end=' ')
    print("FIM!\n", end='')


# Programa Principal
contador(start=1, stop=10, step=1)
contador(start=10, stop=0, step=2)
line()
print("Agora é a sua vez de personalizar a contagem !!!! ")
ini = int(input("Início: "))
st = int(input("Fim: "))
ste = int(input("Passo: "))
contador(ini, st, ste)
