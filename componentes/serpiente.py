import pygame
import sys
import math
import random

class Serpiente:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.vel= 1

    def moverDer(self):
        self.x += self.vel
        

    def moverIz(self):
        self.x += -self.vel

    def dibujar(self, pantalla):
        fsd=1