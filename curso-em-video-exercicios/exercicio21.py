import pygame
pygame.init()

# Carrega e toca o arquivo de música
pygame.mixer.music.load('ex.mp3')
pygame.mixer.music.play()

# Aguarda até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Checa a cada 100 ms se a música ainda está tocando
