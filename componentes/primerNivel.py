import pygame
import sys
import math
import random
import menu
import variables
import serpiente
from pygame.math import Vector2

class Bloque:
    def __init__(self, x, y, color):
        self.pos = Vector2(x, y)
        self.color = color

    def dibujar(self, screen, cell_size):
        rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, rect)

class Nivel:
    def __init__(self, bloques, cell_size):
        self.bloques = bloques
        self.cell_size = cell_size

    def agregar_bloque(self, x, y, color):
        self.bloques.append(Bloque(x, y, color))

    def dibujar(self, screen):
        for bloque in self.bloques:
            bloque.dibujar(screen, self.cell_size)

def nivel1():
    pygame.init()
    cell_size = variables.cell_size
    screen_width, screen_height = variables.pantallaJuego

    screen = pygame.display.set_mode(variables.pantallaJuego)
    pygame.display.set_caption("GravitySnake - Nivel 1")

    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    WHITE = (255, 255, 255)
    SKY_BLUE = (135, 206, 235)

    bloques = [
        Bloque(0, 10, GREEN),
        Bloque(1, 10, GREEN),
        Bloque(2, 10, GREEN),
        Bloque(3, 10, GREEN),
        Bloque(4, 10, GREEN),
        Bloque(5, 10, GREEN),
        Bloque(6, 10, GREEN),
        Bloque(7, 10, GREEN),
        Bloque(8, 10, GREEN),
        Bloque(9, 10, GREEN),
        Bloque(10, 10, GREEN),
        Bloque(11, 10, GREEN),
        Bloque(12, 10, GREEN),
        Bloque(13, 10, GREEN),
        Bloque(14, 10, GREEN),
        Bloque(15, 10, GREEN),
        Bloque(16, 10, GREEN),
        Bloque(17, 10, GREEN),
        Bloque(18, 10, GREEN),
        Bloque(19, 10, GREEN),

        Bloque(8, 9, GREEN),
        Bloque(9, 9, GREEN),
        Bloque(10, 9, GREEN),
        Bloque(11, 9, GREEN),
        Bloque(12, 9, GREEN),
        Bloque(13, 9, GREEN),
        Bloque(10, 8, GREEN),
        Bloque(11, 8, GREEN),
        Bloque(12, 8, GREEN),
    ]
    
    nivel = Nivel(bloques, cell_size)

   
    boton_rect = pygame.Rect(10, 10, 100, 40)
    boton_color = WHITE
    fuente = pygame.font.Font(None, 30)
    texto_boton = fuente.render("Menú", True, BLACK)

    texto_ancho, texto_alto = texto_boton.get_size()
    texto_x = boton_rect.x + (boton_rect.width - texto_ancho) // 2
    texto_y = boton_rect.y + (boton_rect.height - texto_alto) // 2

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if boton_rect.collidepoint(event.pos):
                    menu.menu()  

        screen.fill(SKY_BLUE)
        nivel.dibujar(screen)

        pygame.draw.rect(screen, boton_color, boton_rect)
        screen.blit(texto_boton, (texto_x, texto_y))

        serpiente_obj = serpiente.Serpiente(6, 11, 6, 10, 7, 10)
        serpiente_obj.dibujar(screen)

      
        pygame.display.flip()
        clock.tick(60)




