import pygame
import sys
import math
import random
import menu
import variables
import serpiente

def nivel1():
    pygame.init() 
    cell_size = variables.cell_size
    screen_width, screen_height = variables.pantallaJuego
    
    screen = pygame.display.set_mode(variables.pantallaJuego)
    pygame.display.set_caption("GravitySnake - Nivel 1")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)

    level_layout = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def draw_level():
        for row_index, row in enumerate(level_layout):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    x = col_index * cell_size
                    y = row_index * cell_size
                    pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size))

    clock = pygame.time.Clock()
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_level()
        ser = serpiente.Serpiente(6,11,6,10,7,10);
        ser.dibujar(screen)

        pygame.display.flip()
        clock.tick(60)
