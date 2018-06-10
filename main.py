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
    pygame.display.set_caption("Tarea 2 C. Grafica")
    vista = Vista()
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    pygame.mixer.init()

    # Elementos de la pantalla
    land_objects = [Montana(ancho, 450), Cloud(500, 600), Cloud(1000, 650, 1, -1),
                    Cloud(50, 550, 2, -1), Cloud(900, 625, 2)]
    obj = [Tree(), Tree(), Tree(), Tree(), Tree(), Tree(), Tree(), Tree(), Tree(), Tree()]

    # Reloj del Juego
    clock = pygame.time.Clock()

    # Carga de Sonidos - propiedad de rainymood.com
    pygame.mixer.music.load("sounds/rainymood.ogg")
    pygame.mixer.music.play(-1)

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

        # eventos continuos
        for element in land_objects:
            element.mover()

        # Fondo
        screen.fill((52, 82, 100))

        if len(land_objects) > 0:
            vista.dibujar(land_objects, screen)
        if len(obj) > 0:
            vista.dibujar(obj, screen)

        # vuelca lo dibujado en pantalla
        pygame.display.flip()


main()
