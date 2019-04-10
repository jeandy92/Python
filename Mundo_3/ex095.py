jogadores = list()
jogador = dict()
gols = list()
count = total = gol = 0
while True:

    print("-=" * 30)
    jogador['nome'] = str(input("Nome do Jogador")).title()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou ?"))
    for c in range(0, partidas):
        gol = int(input(f"Quantos gols na partida {c+1} ?"))
        total = total + gol
        gols.append(gol)
        count = count + 1
    opcao = str(input("Quer continuar ? [S/N]")).upper()
    while opcao not in 'nNsS':
        opcao = str(input("Quer continuar ? [S/N]")).upper()
    if opcao in 'Ss':
        jogador['gols'] = gols[:]
        jogador['total'] = total
        jogadores.append(jogador.copy())
        gols.clear()
        gol = 0
        total = 0
        jogador.clear()
    if opcao in 'nN':
        jogador['gols'] = gols[:]
        jogador['total'] = total
        jogadores.append(jogador.copy())
        break
print('\n-=' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 20)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 20)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 parar)"))
    if busca == 999:
        break
    if busca > len(jogadores):
        print(f'ERRO! Não existe jogador com o código{busca}')
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[busca]['nome']}")
        for k, v in enumerate(jogadores[busca]['gols']):
             print(f"       No jogo {k + 1} fez {v} gols")
        print('-=' * 20)
print("volte sempre")