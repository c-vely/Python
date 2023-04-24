import pygame
import time

pygame.mixer.init()
p = pygame.mixer.Sound('output.wav')
p.play()
time.sleep(3)
p.stop()
