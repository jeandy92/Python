from time import sleep

def line():
    print("-=" * 20)


def bigger(*valores):
    line()
    m = 0
    print("Analisando os valores passados....")
    sleep(2.5)
    for num in valores:
        print(num, end=' ')
        sleep(0.4)
        if num > m:
            m = num
    sleep(2.5)
    print(f"Foram informados {len(valores)} ao todo", end=' ')
    sleep(2.5)
    print(f"\nO maior valor informado foi {m}. ")


bigger(2,9,4,5,7,1)
bigger(4,7,0)
bigger(1,2)
bigger(6)
bigger(0)


