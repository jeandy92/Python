import random
import time
from operator import itemgetter

jogadores = dict()
ranking = list()
print("Valores dos dados ")
for c in range(1, 5):
    num = random.randint(1, 6)
    jogadores[f'JOGADOR {c}'] = num
for k, v in jogadores.items():
    print(f'O {k}, tirou {v} no dado.')
    time.sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("=-"*30)
print('  ==== RANKING DE JOGADORES ====')
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]}, com {v[1]} no dado.')
    time.sleep(1)
