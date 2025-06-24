import pygame
import sys
import math
import random
import menu
import bbdd

def login():
    pygame.init()
    pygame.mixer.init()
    sonido_menu = pygame.mixer.Sound("sonido/menu.wav")
    sonido_menu.play(loops=-1)


    NEGRO = (2, 2, 2)
    VERDE = (0, 255, 0)
    BLANCO = (255, 255, 255)
    GRIS = (188, 188, 188)

    COLOR=NEGRO
    COLOR2=GRIS

    WIDTH = 640
    HEIGHT = 480
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravity Snake")

    logo = pygame.image.load('img/logo.jpg')
    logo = pygame.transform.scale(logo, (300, 200))
    logo_rect = logo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))

    fuente = pygame.font.SysFont(None, 30)
    boton = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 60)

    input_text = "Nombre"
    activo = False
    input_box = pygame.Rect(220, 250, 200, 50)

    class Vibora:
        def __init__(self, x):
            self.x = x
            self.y = random.randint(-200, 0)
            self.amp = random.randint(10, 20)
            self.vel = random.uniform(1, 2)
            self.segmentos = 20
            self.separacion = 5
            self.color = VERDE

        def mover(self):
            self.y += self.vel
            if self.y > HEIGHT + 50:
                self.y = random.randint(-200, 0)

        def dibujar(self, pantalla):
            cuerpo = []

            for i in range(self.segmentos):
                y = self.y + i * self.separacion
                x = self.x + math.sin(y * 0.05) * self.amp
                cuerpo.append((int(x), int(y)))

            for i in range(1, len(cuerpo)):
                cx, cy = cuerpo[i]
                color = self.color if i % 2 == 0 else (0, 180, 0)
                pygame.draw.circle(pantalla, color, (cx, cy), 5)

            cabeza_x, cabeza_y = cuerpo[-1]
            pygame.draw.circle(pantalla, (0, 200, 0), (cabeza_x, cabeza_y), 7)

            ojo_offset = 3
            pygame.draw.circle(pantalla, BLANCO, (cabeza_x - ojo_offset, cabeza_y + 2), 2)
            pygame.draw.circle(pantalla, BLANCO, (cabeza_x + ojo_offset, cabeza_y + 2), 2)

            pygame.draw.line(pantalla, (255, 0, 0), (cabeza_x, cabeza_y + 7), (cabeza_x, cabeza_y + 14), 2)
            pygame.draw.line(pantalla, (255, 0, 0), (cabeza_x, cabeza_y + 14), (cabeza_x - 3, cabeza_y + 12), 1)
            pygame.draw.line(pantalla, (255, 0, 0), (cabeza_x, cabeza_y + 14), (cabeza_x + 3, cabeza_y + 12), 1)

    viboras = []
    for _ in range(10):
        lado = random.choice(["izq", "der"])
        if lado == "izq":
            x = random.randint(0, logo_rect.left - 10)
        else:
            x = random.randint(logo_rect.right + 10, WIDTH)
        viboras.append(Vibora(x))

    clock = pygame.time.Clock()
    running = True

    input_text = "Nombre"
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(evento.pos):
                    activo = True
                    input_text=""
                    COLOR2=BLANCO
                elif boton.collidepoint(evento.pos):
                    if input_text == "Nombre" or input_text == "":
                        COLOR = GRIS
                    else:
                        bbdd.agregar(input_text)
                        menu.menu(nombre=input_text)

                #elif boton.collidepoint(evento.pos):
                   # if input_text=="Nombre" or input_text=="":
                     #   COLOR=GRIS
                    #    print("aaa")
                   # else:
                  #      bbdd.agregar(input_text)
                 #       menu.menu()

            if evento.type == pygame.KEYDOWN and activo:
                if evento.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif evento.key == pygame.K_RETURN:
                    print("Entrada:", input_text)
                    input_text = ""
                else:
                    input_text += evento.unicode

        pantalla.fill(NEGRO)

        for v in viboras:
            v.mover()
            v.dibujar(pantalla)

        pantalla.blit(logo, logo_rect)
        pygame.draw.rect(pantalla, BLANCO, input_box, 2)
        text_surface = fuente.render(input_text, True, COLOR2)
        pantalla.blit(text_surface, (input_box.x + 5, input_box.y + 15))

        pygame.draw.rect(pantalla, BLANCO, boton)
        texto = fuente.render("Iniciar", True, NEGRO)
        pantalla.blit(texto, texto.get_rect(center=boton.center))

        texto2 = fuente.render("Ingrese su nombre", True, COLOR)
        pantalla.blit(texto2, (WIDTH // 2 - 93, HEIGHT // 2 + 70))

        pygame.display.flip() 
        clock.tick(60)

    pygame.quit()
    sys.exit()

login()