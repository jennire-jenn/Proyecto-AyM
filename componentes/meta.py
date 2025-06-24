import pygame
from pygame.math import Vector2
import variables

class Meta:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.meta_img = pygame.image.load('img/meta.png').convert_alpha()

    def dibujar(self, pantalla):
        cell_size = variables.cell_size
        x = int(self.pos.x * cell_size)
        y = int(self.pos.y * cell_size)
        meta_rect = pygame.Rect(x, y, cell_size, cell_size)
        pantalla.blit(self.meta_img, meta_rect)

    def colision(self, serpiente):
        return self.pos == serpiente.cuerpo[0]