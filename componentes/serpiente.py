import pygame
import sys
import math
from pygame.math import Vector2
import random
import variables
class Serpiente:
      
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.cuerpo = [Vector2(x1,y1), Vector2(x2,y2), Vector2(x3,y3)]
        self.direccion= Vector2(1,0)
        self.nuevo = False

    def mover(self):
        if self.nuevo == True:
            copia = self.body[:-1]
            copia.insert(0, copia[0], self.direccion)
            self.body = copia[:]
            self.nuevo = False
        else:
            copia = self.body[:-1]
            copia.insert(0, copia[0], self.direccion)
            self.body = copia[:]

    def alargar(self):
        self.nuevo=True

    def caer(self):
        self.direccion = Vector2(0,1)
        self.mover()


    def dibujar(self, pantalla):
        cuadro= variables.cell_size
        for bloque in self.cuerpo:
            x_pos= int(bloque.x*cuadro)
            y_pos= int(bloque.y*cuadro)
            bloque_rect= pygame.Rect(x_pos, y_pos, cuadro, cuadro)
            pygame.draw.rect(pantalla,(0, 255, 0),bloque_rect)