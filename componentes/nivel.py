import pygame
import bloque
class Nivel:
    def __init__(self, bloques, cell_size):
        self.bloques = bloques
        self.cell_size = cell_size

    def agregar_bloque(self, x, y, color):
        self.bloques.append(bloque.Bloque(x, y, color))

    def dibujar(self, screen):
        for bloque in self.bloques:
            bloque.dibujar(screen, self.cell_size)