import random
import pygame
import math
from CC3501Utils import *

# constantes
damage_colors = [(51, 102, 0), (204, 102, 0), (204, 0, 0), (204, 0, 0), (204, 0, 0), (204, 0, 0), (204, 0, 0), (204, 0, 0)]


def generate_mountain(dot_list, left_index, right_index, distance, roughness=.44):
    roughness = roughness
    if left_index + 1 == right_index:
        return
    mid_index = math.floor((left_index + right_index) / 2)
    change = (random.randint(0, 1) * 2 - 1) * distance
    dot_list[mid_index] = max(0, min(720, int(math.floor(
        (dot_list[left_index] + dot_list[right_index])/2 + change))))
    distance *= roughness
    generate_mountain(dot_list, left_index, mid_index, distance)
    generate_mountain(dot_list, mid_index, right_index, distance)


class Montana:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.alto = altura
        self.dots = self.generate()

    def generate(self):
        dot_list = [0] * self.ancho
        dot_list[0] = self.alto
        dot_list[self.ancho-1] = self.alto
        # TODO recursive generation
        generate_mountain(dot_list, 0, self.ancho-1, 250)
        return dot_list

    def dibujar(self, surface):
        for i in range(0, self.ancho):
            pygame.draw.line(surface, (121, 85, 61), (i, 720), (i, 720-self.dots[i]))

    def mover(self):
        pass


class Cloud:
    def generate_y(self):
        lista = [0]*8
        lista[0] = self.pos_y
        lista[7] = self.pos_y
        generate_mountain(lista, 0, 7, 70, .35)
        return lista

    def generate_x(self):
        lista = [0]*8
        for i in range(1, 8):
            lista[i] = lista[i-1] + random.randint(25, 73)
        return lista

    def radious(self):
        x = self.x_list
        y = self.y_list
        radios = [0]*8
        radios[0] = random.randint(35, 60)
        for i in range(1, 8):
            delta_x = int(math.fabs(x[i] - x[i-1]))
            delta_y = int(math.fabs(y[i] - y[i - 1]))
            radios[i] = math.floor(math.sqrt(delta_x**2 + delta_y**2))
        return radios

    def __init__(self, pos_inicial_x, altura, velocidad=1, direccion=1):
        self.pos_x = pos_inicial_x
        self.pos_y = altura
        self.dir = velocidad
        self.vel = direccion
        self.y_list = self.generate_y()
        self.x_list = self.generate_x()
        self.r_list = self.radious()
        color_base = random.randint(150, 230)
        self.color = (color_base, color_base, color_base)

    def change_direction(self):
        self.dir *= -1

    def mover(self):
        self.pos_x += self.dir * self.vel
        if self.pos_x > 1000 or self.pos_x < -50:
            self.change_direction()

    def dibujar(self, surface):
        for i in range(0, 8):
            pygame.draw.circle(surface, self.color, (self.pos_x + self.x_list[i],
                                                     720-self.y_list[i]), self.r_list[i], 0)


class Nulo:
    def __init__(self):
        self.life = 1
        self.damage = 0
        self.collided = True
        self.dotted = False
        self.dots = []

    def dibujar(self, surface):
        pass

    def add_damage(self):
        pass

    def set_collided(self):
        return

    def collide(self, dots):
        pass

    def is_nulo(self):
        return True

    def is_trueno(self):
        return False

    def is_arbol(self):
        return False

    def tick_tock(self):
        return self.life


class Tree:
    def __init__(self):
        self.pos_x = random.randint(20, 1260)
        self.pos_y = random.randint(10, 100)
        self.dir = random.randint(10, 30)
        self.damage = 0
        self.life = 1
        self.color = damage_colors[self.damage]
        self.min_x = 1000
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
        self.collided = True
        self.dotted = False
        self.stack = []  # para ser usado como stack
        # ver:  https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-stacks

    def add_damage(self):
        self.damage += 1

    def is_trueno(self):
        return False

    def is_nulo(self):
        return False

    def is_arbol(self):
        return True

    def tick_tock(self):
        return self.life

    def collide(self, dots):
        if dots == []:
            return
        rect = pygame.Rect(self.min_x, self.min_y, self.max_x - self.min_x, self.max_y-self.min_y)
        # usando https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint
        for pair in dots:
            if rect.collidepoint(pair):
                self.add_damage()
                self.color = damage_colors[self.damage]
                return


    def set_collided(self):
        return

    # Basado en https://www.rosettacode.org/wiki/Fractal_tree#Python
    def iteration(self, s, x1, y1, angle, depth):
        if depth:
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * 5.0)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * 5.0)
            self.min_x = min(self.min_x, x2)
            self.max_x = max(self.max_x, x2)
            self.min_y = min(self.min_y, y2)
            self.max_y = max(self.max_y, y2)
            pygame.draw.line(s, self.color, (x1, y1), (x2, y2), depth)
            self.iteration(s, x2, y2, angle-self.dir, depth-1)
            self.iteration(s, x2, y2, angle+self.dir, depth-1)

    def dibujar(self, surface):
        self.iteration(surface, self.pos_x, 720-self.pos_y, -90, 8)


class Trueno:
    def __init__(self):
        self.pos_x = random.randint(20, 1260)
        self.pos_y = random.randint(20, 150)
        self.dir = random.randint(75, 125)
        self.life = 5
        self.damage = 0
        self.collided = False
        self.dots = []  # Lista de puntos importantes del Trueno
        self.dotted = False

    def is_trueno(self):
        return True

    def is_nulo(self):
        return False

    def is_arbol(self):
        return False

    def set_collided(self):
        self.collided = True

    def tick_tock(self):
        self.life -= 1

    # Basado en la implementación anterior de arboles
    def iteration(self, s, x1, y1, angle, depth):
        color_trueno = (237, 255, 33)
        if depth > 0:
            num = (depth % 2*2)-1
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * 15.0)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * 15.0)
            pygame.draw.line(s, color_trueno, (x1, y1), (x2, y2), depth*2)
            if not self.dotted:  # agregar punto a importantes
                self.dots.append((x2, y2))
            self.iteration(s, x2, y2, angle+22*num, depth-2)
            self.iteration(s, x2, y2, angle+22*num, depth-1)
        else:
            self.dotted = True

    def dibujar(self, surface):
        self.iteration(surface, self.pos_x, self.pos_y, self.dir, 8)
