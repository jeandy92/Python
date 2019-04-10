times = (
    'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro',
    'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG',
    'Vitória', 'Paraná')

print(f'Colocação Final: {times}\n')
print(f'Os 5 primeiros colocados são {times[:5]}')
print(f'Os rebaixados são {times[-4:]}')
print(f'Times em ordem alfabéica: {sorted(times)}')


print(f'A Chapecoense se encontra na {times.index("Chapecoense")+1}º posicao')