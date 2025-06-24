import pygame
import sys
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
import meta

def nivel1(nombre_jugador):
    pygame.init()
    pygame.mixer.init()
    sonido_moneda = pygame.mixer.Sound("sonido/moneda.wav")
    sonido_manzana = pygame.mixer.Sound("sonido/manzana.wav")
    sonido_primernivel = pygame.mixer.Sound("sonido/primernivel.wav")
    sonido_primernivel.set_volume(1)
    sonido_primernivel.play(-1)

    cell_size = variables.cell_size
    screen_width, screen_height = variables.pantallaJuego
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("GravitySnake - Nivel 1")

    NEGRO = (0, 0, 0)
    VERDE = (0, 200, 0)
    BLANCO = (255, 255, 255)
    CELESTE = (135, 206, 235)

    cesped = pygame.image.load('img/cesped.png').convert_alpha()
    tierra = pygame.image.load('img/tierra.png').convert_alpha()
    reiniciar = pygame.image.load('img/r.png').convert_alpha()

    bloques = [
        Bloque(x, 10, VERDE, cesped if x < 8 or x > 13 else tierra) for x in range(20)
    ] + [
        Bloque(8, 7, VERDE, cesped),
        Bloque(8, 8, VERDE, tierra),
        Bloque(8, 9, VERDE, tierra),
        Bloque(9, 7, VERDE, cesped),
        Bloque(9, 8, VERDE, tierra),
        Bloque(9, 9, VERDE, tierra),
        Bloque(10, 9, VERDE, tierra),
        Bloque(11, 9, VERDE, tierra),
        Bloque(12, 9, VERDE, tierra),
        Bloque(13, 9, VERDE, cesped),
        Bloque(10, 8, VERDE, cesped),
        Bloque(11, 8, VERDE, cesped),
        Bloque(12, 8, VERDE, cesped),
    ]

    nivel = Nivel(bloques, cell_size)
    monedas = [moneda.Moneda(11, 6, (255, 223, 0))]
    manzanas = [manzana.Manzana(7, 7)]
    meta_obj = meta.Meta(19, 9)

    boton_rect = pygame.Rect(10, 10, 100, 40)
    boton_color = BLANCO
    fuente = pygame.font.Font(None, 30)
    texto_boton = fuente.render("Menú", True, NEGRO)
    texto_x = boton_rect.x + (boton_rect.width - texto_boton.get_width()) // 2
    texto_y = boton_rect.y + (boton_rect.height - texto_boton.get_height()) // 2

    alto_boton = boton_rect.height
    ancho_reiniciar = int(reiniciar.get_width() * (alto_boton / reiniciar.get_height()))
    reiniciar = pygame.transform.scale(reiniciar, (ancho_reiniciar, alto_boton))
    boton_reiniciar_rect = pygame.Rect(boton_rect.x + boton_rect.width + 10, boton_rect.y, ancho_reiniciar, alto_boton)

    puntuacion = 0
    bbdd.agregar(nombre_jugador)
    jugador_actual = bbdd.veractual()[0]
    id_actual = jugador_actual[0]

    flag = True

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    clock = pygame.time.Clock()
    running = True

    while running:
        if flag:
            serpiente_obj = serpiente.Serpiente(3, 9, 2, 9, 1, 9)
            flag = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bbdd.modificar(puntuacion, id_actual)
                sonido_primernivel.stop()
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                serpiente_obj.caer(bloques)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    serpiente_obj.direccion = Vector2(0, -1)
                elif event.key == pygame.K_DOWN:
                    serpiente_obj.direccion = Vector2(0, 1)
                elif event.key == pygame.K_LEFT:
                    serpiente_obj.direccion = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    serpiente_obj.direccion = Vector2(1, 0)

                serpiente_obj.mover(bloques, forzado=True)
                serpiente_obj.direccion = Vector2(0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_rect.collidepoint(event.pos):
                    bbdd.modificar(puntuacion, id_actual)
                    sonido_primernivel.stop()
                    menu.menu()
                if boton_reiniciar_rect.collidepoint(event.pos):
                    flag = True
                    puntuacion = 0
                    monedas = [moneda.Moneda(11, 6, (255, 223, 0))]
                    manzanas = [manzana.Manzana(7, 7)]

        if serpiente_obj.limite():
            bbdd.modificar(puntuacion, id_actual)
            flag = True
            puntuacion = 0
            monedas = [moneda.Moneda(11, 6, (255, 223, 0))]
            manzanas = [manzana.Manzana(7, 7)]
            continue

        manzana.Manzana.manejar_colisiones(manzanas, serpiente_obj, sonido_manzana)
        puntuacion += moneda.Moneda.manejar_colisiones(monedas, serpiente_obj, sonido_moneda)

        if meta_obj.colision(serpiente_obj):
            bbdd.modificar(puntuacion, id_actual)
            sonido_primernivel.stop()
            menu.menu(nombre_jugador)

        screen.fill(CELESTE)
        nivel.dibujar(screen)
        meta_obj.dibujar(screen)

        for moneda_obj in monedas:
            moneda_obj.dibujar(screen, cell_size)
        for manzana_obj in manzanas:
            manzana_obj.dibujar(screen)
        
        #esto no se esta usando
        serpiente_rect= serpiente_obj.dibujar(screen)
        screen.blit(reiniciar, boton_reiniciar_rect.topleft)
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, NEGRO)
        screen.blit(texto_puntuacion, (screen_width - 200, 10))
        pygame.display.flip()
        clock.tick(60)
