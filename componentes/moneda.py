import pygame
from pygame.math import Vector2

class Moneda:
    def __init__(self, x, y, color):
        self.pos = Vector2(x, y)
        self.color = color
        self.recogida = False
        self.moneda_img = pygame.image.load('img/moneda.png').convert_alpha()

    def dibujar(self, screen, cell_size):
        if not self.recogida:
            rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
            screen.blit(self.moneda_img, rect)
            # pygame.draw.ellipse(screen, self.color, rect)


    def recoger(self):
        self.recogida = True

    @staticmethod
    def manejar_colisiones(monedas, serpiente, sonido_moneda):
        puntuacion = 0
        for moneda in monedas:
            if not moneda.recogida and serpiente.cuerpo[0] == moneda.pos:
                moneda.recoger()
                sonido_moneda.play()
                puntuacion += 500  # Asignar puntos por cada moneda recogida
        return puntuacion