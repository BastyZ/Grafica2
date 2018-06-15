# librerias
import os
from typing import List, Any

import pygame
from CC3501Utils import *
from vista import *
from modelo import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centra la ventana


# Agrega objeto a lista
def agregar(lista, objeto):
    for i in range(0, len(lista)):
        if lista[i].is_nulo():
            lista[i] = objeto
            break


def eliminar(lista, indice):
    lista[indice] = Nulo()


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
                    Cloud(50, 550, 2, -1), Cloud(900, 625, 2), Cloud(100, 600),
                    Cloud(600, 570, 2, -1)]
    obj = [Nulo()]*50
    for i in range(0, 10):
        obj[i] = Tree()

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
                    new = Trueno()
                    agregar(obj, new)
                if event.key == K_m:
                    for i in range(2, random.randint(2, 11)):
                        new = Trueno()
                        agregar(obj, new)
                if event.key == K_a:
                    agregar(obj, Tree())
                if event.key == K_q:
                    run = False

        # eventos continuos
        for element in land_objects:
            element.mover()

        for i in range(0, len(obj)):
            obj[i].tick_tock()
            # Checkear si el objeto debe ser eliminado
            if obj[i].life < 0 or obj[i].damage >= 4:
                eliminar(obj, i)
            # Realizar las colisiones
            if obj[i].is_trueno() and not obj[i].collided:
                if not obj[i].dotted:
                    pass
                else:
                    dots = obj[i].dots
                    obj[i].set_collided()
                    # Agregar los puntos a cada arbol
                    # así nos aseguramos de que sea una vez
                    for j in range(0, len(obj)):
                        if obj[j].is_arbol():
                            obj[j].collide(dots)

        # Fondo
        screen.fill((52, 82, 100))

        if len(land_objects) > 0:
            vista.dibujar(land_objects, screen)
        if len(obj) > 0:
            vista.dibujar(obj, screen)

        # vuelca lo dibujado en pantalla
        pygame.display.flip()


main()
