
#import playsound
#playsound.playsound('audio.mp3', True)

import pygame
pygame.mixer.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait
