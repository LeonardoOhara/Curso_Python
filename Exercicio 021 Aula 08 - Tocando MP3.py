#adicione uma musica mp3 em seu codigo.

print('pai!!!')
#Agora na versão atual tem que colocar input() antes do pygame.event.wait().

import pygame

pygame.init()
pygame.mixer.music.load('big.mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()



