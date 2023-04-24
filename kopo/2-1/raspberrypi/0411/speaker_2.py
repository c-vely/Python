import pygame
import time

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.

p = pygame.mixer.Sound('pu.wav')
p.play()
time.sleep(1)
p.stop()
