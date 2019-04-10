def ficha(nome='<Desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no Campeonato")


# Programa Principal
nome_jogador = str(input("Nome do Jogador: ")).title()
qtd_gols = str(input("Quantos gols foram marcados:"))
if qtd_gols.isnumeric():
    qtd_gols = int(qtd_gols)
else:
    qtd_gols = 0
if nome_jogador.strip() == '':
    ficha(gols=qtd_gols)
else:
    ficha(nome_jogador, qtd_gols)
