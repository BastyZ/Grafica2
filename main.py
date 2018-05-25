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
    init(ancho, alto, "Tarea 2 C. Grafica")
    vista = Vista()

    # Elementos de la pantalla
    land_objects = []
    obj = []

    # Reloj del Juego
    clock = pygame.time.Clock()

    # Main Loop
    while True:
        clock.tick(30)  # FPS


main()
