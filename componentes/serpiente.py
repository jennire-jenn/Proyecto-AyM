import pygame
import sys
import math
from pygame.math import Vector2
import random
import variables
from bloque import Bloque
class Serpiente:
      
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.cuerpo = [Vector2(x1,y1), Vector2(x2,y2), Vector2(x3,y3)]
        self.direccion= Vector2(1,0)
        self.nuevo = False
        self.vel = 5
        self.x = 1

    def mover(self, bloques):
        nueva_cabeza = self.cuerpo[0] + self.direccion
        cabeza_rect = pygame.Rect(
            int(nueva_cabeza.x * variables.cell_size),
            int(nueva_cabeza.y * variables.cell_size),
            variables.cell_size,
            variables.cell_size
        )
        for bloque in bloques:
            bloque_rect = pygame.Rect(
                int(bloque.pos.x * variables.cell_size),
                int(bloque.pos.y * variables.cell_size),
                variables.cell_size,
                variables.cell_size
            )
            if cabeza_rect.colliderect(bloque_rect):
                self.direccion = Vector2(0, 0)
                return 
        if self.nuevo:  
            copia = self.cuerpo[:]
            copia.insert(0, nueva_cabeza)
            self.cuerpo = copia
            self.nuevo = False
        else: 
            copia = self.cuerpo[:-1]
            copia.insert(0, nueva_cabeza)
            self.cuerpo = copia



    def alargar(self):
        self.nuevo=True

    def caer(self):
        self.cuerpo

      #  if self.cuerpo.coliderect(Bloque):
       #     self.vel=0;
       #     self.x=0;
       # else:
       #     self.vel = 5
       #     self.x=1;

       #  if self.cuerpo.coliderect(self.cuerpo):
       #     self.vel=0;
       #     self.x=0;
       # else:
       #     self.vel = 5
       #     self.x=1;

    def monedaSerpiente(self, moneda):
        if not moneda.recogida and self.cuerpo[0] == moneda.pos:
            moneda.recoger()



    def dibujar(self, pantalla):
        cuadro= variables.cell_size
        for bloque in self.cuerpo:
            x_pos= int(bloque.x*cuadro)
            y_pos= int(bloque.y*cuadro)
            bloque_rect= pygame.Rect(x_pos, y_pos, cuadro, cuadro)
            pygame.draw.rect(pantalla,(0, 255, 0),bloque_rect)