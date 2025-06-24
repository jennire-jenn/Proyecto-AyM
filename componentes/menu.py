import pygame
import sys
import primerNivel
import segundoNivel
import tercerNivel
import score





def menu(nombre=None):
    NEGRO = (2, 2, 2)
    print(f"Bienvenido al menú, {nombre}!")

    BLANCO = (255, 255, 255)
    VERDE = (0, 255, 0)

    WIDTH = 640
    HEIGHT = 480
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravity Snake")

    

    fuente = pygame.font.SysFont(None, 30)
    fuente2 = pygame.font.SysFont(None, 50)
    boton1 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 60)

    

    boton2 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 , 200, 60)

    boton3 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 60)

    boton4 = pygame.Rect(WIDTH // 2 + 200, HEIGHT // 2 + 150, 100, 60)


    clock = pygame.time.Clock()
    running = True




    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton1.collidepoint(evento.pos):
                    primerNivel.nivel1()
                elif boton2.collidepoint(evento.pos):
                    segundoNivel.nivel2()
                elif boton3.collidepoint(evento.pos):
                    tercerNivel.nivel3()
                elif boton4.collidepoint(evento.pos):
                    score.score()
            
        pantalla.fill(NEGRO)

        pygame.draw.rect(pantalla, BLANCO, boton1)
        texto1 = fuente.render("Nivel 1", True, NEGRO)
        pantalla.blit(texto1, texto1.get_rect(center=boton1.center))

        pygame.draw.rect(pantalla, BLANCO, boton2)
        texto2 = fuente.render("Nivel 2", True, NEGRO)
        pantalla.blit(texto2, texto2.get_rect(center=boton2.center))

        pygame.draw.rect(pantalla, BLANCO, boton3)
        texto3 = fuente.render("Nivel 3", True, NEGRO)
        pantalla.blit(texto3, texto3.get_rect(center=boton3.center))

        pygame.draw.rect(pantalla, BLANCO, boton4)
        texto4 = fuente.render("Scores", True, NEGRO)
        pantalla.blit(texto4, texto4.get_rect(center=boton4.center))

        texto4 = fuente2.render("Elija un nivel", True, BLANCO)
        pantalla.blit(texto4, (WIDTH // 2 -110, HEIGHT // 2 - 180))



        pygame.display.flip()  
        clock.tick(60)