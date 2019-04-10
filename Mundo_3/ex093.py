jogadores = dict()
gols = list()
count = total = 0
jogadores['nome'] = str(input("Nome do Jogador:")).title()
partidas = int(input(f"Quantas Partidas {jogadores['nome']} jogou:"))
while count < partidas:
    gol = int(input(f"Quantos gols na partida {count} ?"))
    total = total + gol
    gols.append(gol)
    count = count + 1
count = 0
jogadores['gols'] = gols
jogadores['total'] = total
print("-="*30)
print(jogadores)
print("-="*30)
for k,v in jogadores.items():
    if k == 'nome':
        print(f"O nome do Jogador {jogadores['nome']}")
    if k == 'gols':
        print(f"Marcou{jogadores['gols']} gols")
    if k == 'total':
        print(f"Ao todo foram {jogadores['total']} gols ")
print("-="*30)
print(f"O jogador {jogadores['nome']} jogou {len(jogadores['gols'])} partidas")
while count < partidas:
    print(f"=> Na partida {count}, fez {jogadores['gols'][count]} gols")
    count = count + 1
