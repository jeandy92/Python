import time, emoji

for c in range(10, 0, -1):
    print('{}'.format(c))
    time.sleep(1)
print(emoji.emojize(':fireworks:', use_aliases=True))
print('\n Feliz Ano novo !!!!')
