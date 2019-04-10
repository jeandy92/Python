
import pygame

cidade = str(input('Nome da Cidade: ')).split()

if 'SANTO' in cidade[0]:
    print("Cidade começa com SANTO: {}".format(cidade[0]))
    pygame.mixer.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait
else:
    print('Cidade não começa com Santos: {}'.format(cidade[0]))


