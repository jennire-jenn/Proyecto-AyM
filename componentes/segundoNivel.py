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


def nivel2(nombre_jugador):
    pygame.init()
    pygame.mixer.init()
    sonido_moneda = pygame.mixer.Sound("sonido/moneda.wav")
    sonido_manzana = pygame.mixer.Sound("sonido/manzana.wav")
    cell_size = variables.cell_size
    screen_width, screen_height = variables.pantallaJuego
    screen = pygame.display.set_mode(variables.pantallaJuego)
    pygame.display.set_caption("GravitySnake - Nivel 2")

    NEGRO = (0, 0, 0)
    VERDE = (0, 200, 0)
    BLANCO = (255, 255, 255)
    CELESTE = (135, 206, 235)

    cesped= pygame.image.load('img/cesped.png').convert_alpha()
    tierra= pygame.image.load('img/tierra.png').convert_alpha()
    reiniciar = pygame.image.load('img/r.png').convert_alpha()

    bloques = [
        Bloque(1, 9, VERDE,cesped),
        Bloque(2, 9, VERDE,cesped),
        Bloque(3, 9, VERDE,cesped),
        Bloque(3, 5, VERDE,cesped),
        Bloque(3, 6, VERDE,tierra),
        Bloque(3, 7, VERDE,tierra),
        Bloque(4, 9, VERDE,cesped),

        Bloque(7, 7, VERDE,cesped),
        Bloque(6, 5, VERDE,cesped),
        Bloque(7, 5, VERDE,cesped),

        Bloque(8, 9, VERDE,cesped),
        Bloque(9, 9, VERDE,cesped),
        Bloque(10, 9, VERDE,cesped),
        Bloque(11, 9, VERDE,cesped),

        Bloque(11, 11, VERDE,cesped),
        Bloque(11, 12, VERDE,tierra),
        Bloque(11, 13, VERDE,tierra),
        Bloque(11, 14, VERDE,tierra),
        Bloque(12, 11, VERDE,cesped),
        Bloque(13, 11, VERDE,cesped),

        Bloque(11, 15, VERDE,tierra),
        Bloque(11, 16, VERDE,tierra),
        Bloque(12, 16, VERDE,cesped),
        Bloque(13, 16, VERDE,cesped),
        Bloque(14, 16, VERDE,cesped),
        Bloque(15, 16, VERDE,cesped),
    ]
    
    nivel = Nivel(bloques, cell_size)

    monedas = [
                moneda.Moneda(17, 12, (255, 223, 0)),
            ]
    manzanas = [
            manzana.Manzana(5, 7),
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

    alto_boton_menu = boton_rect.height
    ancho_boton_reiniciar = int(reiniciar.get_width() * (alto_boton_menu / reiniciar.get_height()))
    reiniciar = pygame.transform.scale(reiniciar, (ancho_boton_reiniciar, alto_boton_menu))

    boton_reiniciar_rect = pygame.Rect(
        boton_rect.x + boton_rect.width + 10,  
        boton_rect.y,
        ancho_boton_reiniciar,  
        alto_boton_menu 
    )    
    while running:      
        while flag:
         serpiente_obj = serpiente.Serpiente(3, 7, 2, 7, 1, 7)
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
                    print("Reiniciando nivel")
                    flag = True 
                    puntuacion = 0 
                    monedas = [
                        moneda.Moneda(17, 12, (255, 223, 0)),
                    ]
                    manzanas = [
                        manzana.Manzana(5, 7),
                    ]
                    continue
            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                    if boton_rect.collidepoint(event.pos):
                        bbdd.modificar(puntuacion, id_actual)            
                        menu.menu()  
                    if boton_reiniciar_rect.collidepoint(event.pos):  
                        flag = True 
                        puntuacion = 0 
                        monedas = [
                                    moneda.Moneda(17, 12, (255, 223, 0)),
                                ]
                        manzanas = [
                                manzana.Manzana(5, 7),
                                ]            
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
        screen.blit(reiniciar, boton_reiniciar_rect.topleft)
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, NEGRO)
        screen.blit(texto_puntuacion, (screen_width - 200, 10))
        pygame.display.flip()
        clock.tick(60)
