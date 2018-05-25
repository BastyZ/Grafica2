# librerias
import os
import pygame
from CC3501Utils import *
from vista import *
from modelo import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centra la ventana


def main():
    ancho = 1280
    alto = 720
    screen = pygame.display.set_mode((ancho, alto))
    # init(ancho, alto, "Tarea 2 C. Grafica")
    vista = Vista()

    # Elementos de la pantalla
    land_objects = []
    obj = []

    # Reloj del Juego
    clock = pygame.time.Clock()

    # Main Loop
    run = True
    while run:
        clock.tick(30)  # FPS

        # Eventos en el juego
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            # Keydown events
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    print("1 rayo lanzado")
                    # TODO lanzar rayo
                    # verificar colisiones con arboles
                if event.key == K_m:
                    print("random rayos lanzados")
                    # TODO lanzar random(2,10) rayos
                if event.key == K_a:
                    print("crear arbol")
                    # TODO crear arbol
                if event.key == K_q:
                    run = False

        #Fondo
        screen.fill((52, 82, 100))

        # vuelca lo dibujado en pantalla
        pygame.display.flip()


main()
