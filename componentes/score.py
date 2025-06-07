import pygame
import sys
import bbdd
def score():
    NEGRO = (2, 2, 2)
    
    BLANCO = (255, 255, 255)

    WIDTH = 640
    HEIGHT = 480
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravity Snake")

    

    fuente = pygame.font.SysFont(None, 30)
    fuente2 = pygame.font.SysFont(None, 50)
    


    clock = pygame.time.Clock()
    running = True

    jugadores=bbdd.ver()
    
    nombre1 = jugadores[0]
    nombre2 = jugadores[1]
    nombre3 = jugadores[2]
    nombre4 = jugadores[3]
    nombre5 = jugadores[4]

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            
                    


    
        pantalla.fill(NEGRO)

        

        texto1 = fuente2.render("HIGH SCORES", True, BLANCO)
        pantalla.blit(texto1, (WIDTH // 2 -110, HEIGHT // 2 - 180))

        texto2 = fuente.render(nombre1, True, BLANCO)
        pantalla.blit(texto2, (WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 60))
        texto3 = fuente.render(nombre2, True, BLANCO)
        pantalla.blit(texto3, (WIDTH // 2 - 100, HEIGHT // 2 , 200, 60))
        texto4 = fuente.render(nombre3, True, BLANCO)
        pantalla.blit(texto4, (WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 60))
        texto5 = fuente.render(nombre4, True, BLANCO)
        pantalla.blit(texto5, (WIDTH // 2 - 100, HEIGHT // 2 + 200, 200, 60))
        texto6 = fuente.render(nombre5, True, BLANCO)
        pantalla.blit(texto6, (WIDTH // 2 - 100, HEIGHT // 2 + 300, 200, 60))



        pygame.display.flip()  
        clock.tick(60)