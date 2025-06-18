import pygame
from pygame.math import Vector2
import variables
from bloque import Bloque
class Serpiente:
      
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.cuerpo = [Vector2(x1,y1), Vector2(x2,y2), Vector2(x3,y3)]
        self.direccion= Vector2(1,0)
        self.nuevo = False

    def mover(self, bloques, forzado=True):
        nueva_cabeza = self.cuerpo[0] + self.direccion

        nueva_cabeza = self.cuerpo[0] + self.direccion
        if nueva_cabeza in self.cuerpo:
            return
        cabeza_rect = pygame.Rect(
            int(nueva_cabeza.x * variables.cell_size),
            int(nueva_cabeza.y * variables.cell_size),
            variables.cell_size,
            variables.cell_size
        )
        colision = False
        for bloque in bloques:
            bloque_rect = pygame.Rect(
                int(bloque.pos.x * variables.cell_size),
                int(bloque.pos.y * variables.cell_size),
                variables.cell_size,
                variables.cell_size
            )
            if cabeza_rect.colliderect(bloque_rect):
                colision = True
                break  

        if colision and not forzado:
            return  

        if colision and forzado:
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

    def caer(self, bloques):
        if not self.esta_sostenida(bloques):
            nuevo_cuerpo = []
            for segmento in self.cuerpo:
                nueva_pos = segmento + Vector2(0, 1)
                nuevo_cuerpo.append(nueva_pos)
            self.cuerpo = nuevo_cuerpo

    def monedaSerpiente(self, moneda):
        if not moneda.recogida and self.cuerpo[0] == moneda.pos:
            moneda.recoger()

    def limite(self):
        cabeza = self.cuerpo[0] 
        if cabeza.x < 0 or cabeza.x >= variables.cell_number or cabeza.y < 0 or cabeza.y >= variables.cell_number:
            print("Saliste de los límites del nivel")
            return True
        return False

    def dibujar(self, pantalla):
        cuadro= variables.cell_size
        serpiente_rect = []
        for bloque in self.cuerpo:
            x_pos= int(bloque.x*cuadro)
            y_pos= int(bloque.y*cuadro)
            bloque_rect= pygame.Rect(x_pos, y_pos, cuadro, cuadro)
            pygame.draw.rect(pantalla,(0, 255, 0),bloque_rect)
            serpiente_rect.append(bloque_rect)
        return serpiente_rect
    
    def esta_sostenida(self, bloques):
        for segmento in self.cuerpo:
            debajo = segmento + Vector2(0, 1)
            for bloque in bloques:
                if debajo == bloque.pos:
                    return True  
        return False  
            