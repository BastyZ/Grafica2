# librerias
import os
import pygame
import CC3501Utils

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centra la ventana

def main():
    ancho = 1280
    alto = 720
    init(ancho, alto, "Tarea 2 C. Grafica")

    # Elementos de la pantalla
    land_objects = []
    obj = []

    # Reloj del Juego
    clock = pygame.time.Clock()


    # Main Loop
    while True:
        clock.tick(30)  # FPS
