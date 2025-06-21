import pygame
import sys
import math
import random
import menu
import variables
import serpiente
from pygame.math import Vector2
import moneda
import manzana
from bloque import Bloque
from nivel import Nivel
import bbdd


def nivel3(nombre_jugador):
    pygame.init()
    pygame.mixer.init()
    sonido_moneda = pygame.mixer.Sound("sonido/moneda.wav")
    sonido_manzana = pygame.mixer.Sound("sonido/manzana.wav")
    cell_size = variables.cell_size
    screen_width, screen_height = variables.pantallaJuego
    screen = pygame.display.set_mode(variables.pantallaJuego)
    pygame.display.set_caption("GravitySnake - Nivel 3")

    NEGRO = (0, 0, 0)
    VERDE = (0, 200, 0)
    BLANCO = (255, 255, 255)
    CELESTE = (135, 206, 235)

    cesped= pygame.image.load('img/cesped.png').convert_alpha()
    tierra= pygame.image.load('img/tierra.png').convert_alpha()

    bloques = [
        Bloque(0, 8, VERDE,cesped),  
        Bloque(1, 8, VERDE,cesped),
        Bloque(2, 8, VERDE,cesped),
        Bloque(3, 8, VERDE,cesped),
        Bloque(4, 8, VERDE,cesped),
        Bloque(5, 8, VERDE,cesped),
        Bloque(5, 9, VERDE,cesped),
        Bloque(6, 9, VERDE,cesped),
        Bloque(7, 9, VERDE,cesped),
        Bloque(7, 8, VERDE,cesped),
        Bloque(7, 7, VERDE,cesped),
        Bloque(7, 6, VERDE,cesped),
        Bloque(7, 5, VERDE,cesped),
        Bloque(4, 6, VERDE,cesped),
        Bloque(4, 5, VERDE,cesped),
        Bloque(5, 5, VERDE,cesped),
        Bloque(7, 5, VERDE,cesped),         
        Bloque(9, 5, VERDE,cesped),
        
        #puente
        Bloque(9, 0, VERDE,cesped),
        Bloque(9, 1, VERDE,cesped),
        Bloque(9, 2, VERDE,cesped),
        Bloque(9, 3, VERDE,cesped),
        Bloque(9, 4, VERDE,cesped),
        Bloque(9, 5, VERDE,cesped),
        Bloque(9, 6, VERDE,cesped),
        Bloque(9, 7, VERDE,cesped),        
        Bloque(9, 8, VERDE,cesped),
        Bloque(9, 9, VERDE,cesped),
        Bloque(9, 10, VERDE,cesped),
        
        #3B  
        Bloque(10, 17, VERDE,cesped),
        Bloque(12, 17, VERDE,cesped),
        Bloque(14, 17, VERDE,cesped),
        Bloque(16, 17, VERDE,cesped),

        Bloque(8, 14, VERDE,cesped),
        Bloque(9, 14, VERDE,cesped),
        Bloque(10, 14, VERDE,cesped),
        Bloque(10, 15, VERDE,cesped),
        Bloque(10, 16, VERDE,cesped),
        Bloque(10, 18, VERDE,cesped),
        Bloque(11, 18, VERDE,cesped),
        Bloque(12, 16, VERDE,cesped),
        Bloque(12, 16, VERDE,cesped),
        Bloque(13, 16, VERDE,cesped),
        Bloque(13, 16, VERDE,cesped),
        Bloque(14, 19, VERDE,cesped),
        Bloque(15, 19, VERDE,cesped),
        Bloque(16, 19, VERDE,cesped),
        Bloque(14, 16, VERDE,cesped),
        Bloque(14, 18, VERDE,cesped),
        Bloque(12, 18, VERDE,cesped),
        Bloque(16, 16, VERDE,cesped),
        Bloque(16, 18, VERDE,cesped),
        Bloque(16, 16, VERDE,cesped),
        Bloque(16, 15, VERDE,cesped),
        Bloque(16, 14, VERDE,cesped),
        Bloque(12, 14, VERDE,cesped),
        Bloque(13, 14, VERDE,cesped),
        Bloque(14, 14, VERDE,cesped),
    ]
    
    nivel = Nivel(bloques, cell_size)
    #moneda_obj = moneda.Moneda(16, 12, (255, 223, 0))
    #manzana_obj = manzana.Manzana(7, 8)
    #moneda_ob = moneda.Moneda(16, 11, (255, 223, 0))

    monedas = [
                moneda.Moneda(17, 12, (255, 223, 0)),
                #moneda.Moneda(3, 3, (255, 223, 0))
            ]
    manzanas = [
            manzana.Manzana(5, 6),
            manzana.Manzana(13, 15),
            #manzana.Manzana(12, 8)
            ]

    boton_rect = pygame.Rect(10, 10, 100, 40)
    boton_color = BLANCO
    fuente = pygame.font.Font(None, 30)
    texto_boton = fuente.render("Menú", True, NEGRO)
    texto_ancho, texto_alto = texto_boton.get_size()
    texto_x = boton_rect.x + (boton_rect.width - texto_ancho) // 2
    texto_y = boton_rect.y + (boton_rect.height - texto_alto) // 2

    puntuacion = 0 
    clock = pygame.time.Clock()
    running = True
    flag= True
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,150)

    bbdd.agregar(nombre_jugador)
    jugador_actual = bbdd.veractual()[0]
    id_actual = jugador_actual[0]
    
    while running:      
        while flag:
         serpiente_obj = serpiente.Serpiente(2, 7, 1, 7, 0, 7)
         flag = False


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bbdd.modificar(puntuacion, id_actual)  
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    serpiente_obj.caer(bloques)
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        serpiente_obj.direccion = Vector2(0,-1)
                        serpiente_obj.mover(bloques, forzado=True)
                        serpiente_obj.direccion = Vector2(0,0)
                    if event.key == pygame.K_RIGHT:
                        serpiente_obj.direccion = Vector2(1,0)
                        serpiente_obj.mover(bloques, forzado=True)
                        serpiente_obj.direccion = Vector2(0,0)
                    if event.key == pygame.K_DOWN:
                        serpiente_obj.direccion = Vector2(0,1)
                        serpiente_obj.mover(bloques, forzado=True)
                        serpiente_obj.direccion = Vector2(0,0)
                    if event.key == pygame.K_LEFT:
                        serpiente_obj.direccion = Vector2(-1,0)
                        serpiente_obj.mover(bloques, forzado=True)
                        serpiente_obj.direccion = Vector2(0,0)
                if serpiente_obj.limite():
                    bbdd.modificar(puntuacion, id_actual) 
                    nivel3()
                    pygame.quit() 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                    if boton_rect.collidepoint(event.pos):
                        bbdd.modificar(puntuacion, id_actual)            
                        menu.menu()  
             
        manzana.Manzana.manejar_colisiones(manzanas, serpiente_obj, sonido_manzana)
        puntuacion += moneda.Moneda.manejar_colisiones(monedas, serpiente_obj, sonido_moneda)
        screen.fill(CELESTE)
        nivel.dibujar(screen)
        for moneda_obj in monedas:
                    moneda_obj.dibujar(screen, cell_size)
                    serpiente_obj.dibujar(screen)
        for manzana_obj in manzanas:
                        manzana_obj.dibujar(screen)

        serpiente_obj.dibujar(screen)

        pygame.draw.rect(screen, boton_color, boton_rect)
        screen.blit(texto_boton, (texto_x, texto_y))
        moneda_obj.dibujar(screen, cell_size)
        manzana_obj.dibujar(screen)
        serpiente_obj.monedaSerpiente(moneda_obj)

        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, NEGRO)
        screen.blit(texto_puntuacion, (screen_width - 200, 10))
        pygame.display.flip()
        clock.tick(60)
