import pygame
import sys
import math
import random
import menu

def nivel1():
    a=1
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("GravitySnake - Nivel 1")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)

    block_size = 40
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
                    x = col_index * block_size
                    y = row_index * block_size
                    pygame.draw.rect(screen, GREEN, (x, y, block_size, block_size))

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_level()

        pygame.display.flip()
        clock.tick(60)