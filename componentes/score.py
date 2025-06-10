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
    
    nombre1 = "1. "+str(jugadores[0][1])+"  "+str(jugadores[0][2])
    nombre2 = "2. "+str(jugadores[1][1])+"  "+str(jugadores[1][2])
    nombre3 = "3. "+str(jugadores[2][1])+"  "+str(jugadores[2][2])
    nombre4 = "4. "+str(jugadores[3][1])+"  "+str(jugadores[3][2])
    nombre5 = "5. "+str(jugadores[4][1])+"  "+str(jugadores[4][2])

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
        pantalla.blit(texto2, (WIDTH // 2 - 100, HEIGHT // 2 - 100))
        texto3 = fuente.render(nombre2, True, BLANCO)
        pantalla.blit(texto3, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        texto4 = fuente.render(nombre3, True, BLANCO)
        pantalla.blit(texto4, (WIDTH // 2 - 100, HEIGHT // 2 ))
        texto5 = fuente.render(nombre4, True, BLANCO)
        pantalla.blit(texto5, (WIDTH // 2 - 100, HEIGHT // 2 + 50))
        texto6 = fuente.render(nombre5, True, BLANCO)
        pantalla.blit(texto6, (WIDTH // 2 - 100, HEIGHT // 2 + 100))



        pygame.display.flip()  
        clock.tick(60)