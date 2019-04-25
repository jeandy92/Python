palavras = ('Alavanca',
            'Esteroides', 'Natal', 'Menino', 'Oxigenio', 'Amputar', 'Enfurecer', 'Tímido', 'Todo', 'Sonhar',
            'Alimentacao', 'Morto', 'Lancamento', 'Temperatura', 'Maca', 'Cultura', 'ubere', 'Quilometros',
            'Dinossauro', 'Abaixo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
