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

    b= pygame.image.load('img/bloque.png').convert_alpha()
    b2= pygame.image.load('img/bloque2.png').convert_alpha()
    b3= pygame.image.load('img/bloque3.png').convert_alpha()
    reiniciar = pygame.image.load('img/r.png').convert_alpha()

    bloques = [
        Bloque(0, 8, VERDE,b),  
        Bloque(1, 8, VERDE,b2),
        Bloque(2, 8, VERDE,b3),
        Bloque(3, 8, VERDE,b),
        Bloque(4, 8, VERDE,b2),
        Bloque(5, 8, VERDE,b3),
        Bloque(5, 9, VERDE,b),
        Bloque(6, 9, VERDE,b2),
        Bloque(7, 9, VERDE,b3),
        Bloque(7, 8, VERDE,b2),
        Bloque(7, 7, VERDE,b3),
        Bloque(7, 6, VERDE,b),
        Bloque(7, 5, VERDE,b2),
        Bloque(4, 6, VERDE,b3),
        Bloque(4, 5, VERDE,b),
        Bloque(5, 5, VERDE,b2),
        Bloque(7, 5, VERDE,b3),         
        Bloque(9, 5, VERDE,b),      
        #puente
        Bloque(9, 0, VERDE,b),
        Bloque(9, 1, VERDE,b2),
        Bloque(9, 2, VERDE,b3),
        Bloque(9, 3, VERDE,b),
        Bloque(9, 4, VERDE,b2),
        Bloque(9, 5, VERDE,b3),
        Bloque(9, 6, VERDE,b),
        Bloque(9, 7, VERDE,b2),        
        Bloque(9, 8, VERDE,b3),
        Bloque(9, 9, VERDE,b),
        Bloque(9, 10, VERDE,b2),
        #3B  
        Bloque(17, 13, VERDE,b3),
        Bloque(18, 13, VERDE,b2),
        Bloque(19, 13, VERDE,b),
        Bloque(10, 17, VERDE,b2),
        Bloque(12, 17, VERDE,b3),
        Bloque(14, 17, VERDE,b3),
        Bloque(16, 17, VERDE,b2),
        Bloque(8, 13, VERDE,b2),
        Bloque(9, 13, VERDE,b3),
        Bloque(10, 13, VERDE,b),
        Bloque(10, 14, VERDE,b2),
        Bloque(10, 15, VERDE,b3),
        Bloque(10, 16, VERDE,b),
        Bloque(10, 18, VERDE,b),
        Bloque(11, 18, VERDE,b3),
        Bloque(12, 16, VERDE,b),
        Bloque(12, 16, VERDE,b2),
        Bloque(13, 16, VERDE,b3),
        Bloque(13, 16, VERDE,b),
        Bloque(14, 19, VERDE,b2),
        Bloque(15, 19, VERDE,b3),
        Bloque(16, 19, VERDE,b),
        Bloque(14, 16, VERDE,b2),
        Bloque(14, 18, VERDE,b3),
        Bloque(12, 18, VERDE,b),
        Bloque(16, 16, VERDE,b),
        Bloque(16, 18, VERDE,b3),
        Bloque(16, 16, VERDE,b),
        Bloque(16, 15, VERDE,b3),
        Bloque(16, 13, VERDE,b3),
        Bloque(16, 13, VERDE,b),
        Bloque(12, 13, VERDE,b2),
        Bloque(13, 13, VERDE,b3),
        Bloque(14, 13, VERDE,b),
        Bloque(16, 14, VERDE,b2),
        Bloque(12, 14, VERDE,b3),
        Bloque(13, 14, VERDE,b),
        Bloque(14, 14, VERDE,b2),
    ]
    
    nivel = Nivel(bloques, cell_size)
    monedas = [
                moneda.Moneda(8, 9, (255, 223, 0)),
                moneda.Moneda(11, 13, (255, 223, 0))    
            ]
    manzanas = [
            manzana.Manzana(5, 6),
            manzana.Manzana(13, 15),
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
                    print("Reiniciando nivel")
                    flag = True 
                    monedas = [
                        moneda.Moneda(17, 12, (255, 223, 0)),
                    ]
                    manzanas = [
                        manzana.Manzana(5, 6),
                        manzana.Manzana(13, 15),                    ]
                    continue
            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                    if boton_rect.collidepoint(event.pos):
                        bbdd.modificar(puntuacion, id_actual)            
                        menu.menu()  
                    if boton_reiniciar_rect.collidepoint(event.pos):  
                        flag = True 
                        puntuacion = 0  
                        monedas = [
                                    moneda.Moneda(8, 9, (255, 223, 0)),
                                    moneda.Moneda(11, 13, (255, 223, 0))    
                                ]
                        manzanas = [
                                manzana.Manzana(5, 6),
                                manzana.Manzana(13, 15),
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
