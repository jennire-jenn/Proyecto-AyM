import pygame
from pygame.math import Vector2

class Bloque:
    def __init__(self, x, y, color):
        self.pos = Vector2(x, y)
        self.color = color

    def dibujar(self, screen, cell_size):
        rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, rect)