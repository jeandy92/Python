def area(largura, comprimento):
    area = largura * comprimento
    print(f"A Area de um Terreno {largura}x{comprimento} é de {area}m²")


def titulo(txt):
    print("-=" * 30)
    print(txt.title())
    print("-=" * 30)


# Programa Principal
titulo("controle de terreno")
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))

area(largura, comprimento)
