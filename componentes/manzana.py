import pygame
from pygame.math import Vector2
import variables

class Manzana:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.visible = True

    def dibujar(self, pantalla):
        if self.visible:
            cell_size = variables.cell_size
            x = int(self.pos.x * cell_size + cell_size / 2)
            y = int(self.pos.y * cell_size + cell_size / 2)
            pygame.draw.circle(pantalla, (255, 0, 0), (x, y), cell_size // 2)

    def desaparecer(self):
        self.visible = False