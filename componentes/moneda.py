import pygame
from pygame.math import Vector2

class Moneda:
    def __init__(self, x, y, color):
        self.pos = Vector2(x, y)
        self.color = color
        self.recogida = False

    def dibujar(self, screen, cell_size):
        if not self.recogida:
            rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
            pygame.draw.ellipse(screen, self.color, rect)

    def recoger(self):
        self.recogida = True
