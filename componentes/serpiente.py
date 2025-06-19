import pygame
from pygame.math import Vector2
import variables
from bloque import Bloque
class Serpiente:
      
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.cuerpo = [Vector2(x1,y1), Vector2(x2,y2), Vector2(x3,y3)]
        self.direccion= Vector2(1,0)
        self.nuevo = False

        self.cabeza_arriba = pygame.image.load('img/cabeza_arriba.png').convert_alpha()
        self.cabeza_abajo = pygame.image.load('img/cabeza_abajo.png').convert_alpha()
        self.cabeza_der = pygame.image.load('img/cabeza_der.png').convert_alpha()
        self.cabeza_izq = pygame.image.load('img/cabeza_izq.png').convert_alpha()

        self.vertical = pygame.image.load('img/vertical.png').convert_alpha()
        self.horizontal = pygame.image.load('img/horizontal.png').convert_alpha()
        
        self.cuerpo_tr = pygame.image.load('img/cuerpo_tr.png').convert_alpha()
        self.cuerpo_tl = pygame.image.load('img/cuerpo_tl.png').convert_alpha()
        self.cuerpo_br = pygame.image.load('img/cuerpo_br.png').convert_alpha()
        self.cuerpo_bl = pygame.image.load('img/cuerpo_bl.png').convert_alpha()

        self.cola_arriba = pygame.image.load('img/cola_arriba.png').convert_alpha()
        self.cola_abajo = pygame.image.load('img/cola_abajo.png').convert_alpha()
        self.cola_der = pygame.image.load('img/cola_der.png').convert_alpha()
        self.cola_izq = pygame.image.load('img/cola_izq.png').convert_alpha()

        

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
        self.orientacion_cabeza()
        self.orientacion_cola()

        for i,bloque in enumerate(self.cuerpo):
            x_pos = int(bloque.x * variables.cell_size)
            y_pos = int(bloque.y * variables.cell_size)
            bloque_rect = pygame.Rect(x_pos,y_pos,variables.cell_size,variables.cell_size)
            if i == 0:
                pantalla.blit(self.cabeza,bloque_rect)
            elif i == len(self.cuerpo) - 1:
                pantalla.blit(self.tail,bloque_rect)
            else:
                bloque_anterior = self.cuerpo[i + 1] - bloque
                bloque_siguiente = self.cuerpo[i - 1] - bloque
                if bloque_anterior.x == bloque_siguiente.x:
                    pantalla.blit(self.vertical,bloque_rect)
                elif bloque_anterior.y == bloque_siguiente.y:
                    pantalla.blit(self.horizontal,bloque_rect)
                else:
                    if bloque_anterior.x == -1 and bloque_siguiente.y == -1 or bloque_anterior.y == -1 and bloque_siguiente.x == -1:
                        pantalla.blit(self.cuerpo_tl,bloque_rect)
                    elif bloque_anterior.x == -1 and bloque_siguiente.y == 1 or bloque_anterior.y == 1 and bloque_siguiente.x == -1:
                        pantalla.blit(self.cuerpo_bl,bloque_rect)
                    elif bloque_anterior.x == 1 and bloque_siguiente.y == -1 or bloque_anterior.y == -1 and bloque_siguiente.x == 1:
                        pantalla.blit(self.cuerpo_tr,bloque_rect)
                    elif bloque_anterior.x == 1 and bloque_siguiente.y == 1 or bloque_anterior.y == 1 and bloque_siguiente.x == 1:
                        pantalla.blit(self.cuerpo_br,bloque_rect)

    def orientacion_cabeza(self):
        orientacion = self.cuerpo[1] - self.cuerpo[0]
        if orientacion == Vector2(1,0): self.cabeza = self.cabeza_izq
        elif orientacion == Vector2(-1,0): self.cabeza = self.cabeza_der
        elif orientacion == Vector2(0,1): self.cabeza = self.cabeza_arriba
        elif orientacion == Vector2(0,-1): self.cabeza = self.cabeza_abajo

    def orientacion_cola(self):
        orientacion = self.cuerpo[-2] - self.cuerpo[-1]
        if orientacion == Vector2(1,0): self.tail = self.cola_izq
        elif orientacion == Vector2(-1,0): self.tail = self.cola_der
        elif orientacion == Vector2(0,1): self.tail = self.cola_arriba
        elif orientacion == Vector2(0,-1): self.tail = self.cola_abajo
    
    def esta_sostenida(self, bloques):
        for segmento in self.cuerpo:
            debajo = segmento + Vector2(0, 1)
            for bloque in bloques:
                if debajo == bloque.pos:
                    return True  
        return False  
            