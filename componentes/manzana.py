import pygame
from pygame.math import Vector2
import variables

class Manzana:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.visible = True
        self.manzana_img = pygame.image.load('img/manzana2.png').convert_alpha()

    def dibujar(self, pantalla):
        if self.visible:
            cell_size = variables.cell_size
            x = int(self.pos.x * cell_size)
            y = int(self.pos.y * cell_size)
            manzana_rect = pygame.Rect(x, y, cell_size, cell_size)
            pantalla.blit(self.manzana_img, manzana_rect)
            #pygame.draw.circle(pantalla, (255, 0, 0), (x, y), cell_size // 2)

    def desaparecer(self):
        self.visible = False

    @staticmethod
    def manejar_colisiones(manzanas, serpiente, sonido_manzana):
        """Maneja la interacción entre la serpiente y las manzanas."""
        for manzana in manzanas:
            if manzana.visible and serpiente.cuerpo[0] == manzana.pos:
                manzana.desaparecer()
                sonido_manzana.play()
                serpiente.alargar()  # La serpiente crece al comer una manzana
