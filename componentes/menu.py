import pygame
import sys
import math
import random


NEGRO = (2, 2, 2)
VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)
WIDTH = 640
HEIGHT = 480
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Snake")
clock = pygame.time.Clock()

def menu():

    running = True


    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            
    
        pantalla.fill(NEGRO)
        pygame.display.flip()  
        clock.tick(60)

pygame.quit()
sys.exit()