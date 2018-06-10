import random
import math
from CC3501Utils import *


def generate_mountain(dot_list, left_index, right_index, distance, roughness=.44):
    roughness = roughness
    if left_index + 1 == right_index:
        return
    mid_index = math.floor((left_index + right_index) / 2)
    change = (random.randint(0, 1) * 2 - 1) * distance
    dot_list[mid_index] = max(0, min(720, int(math.floor((dot_list[left_index] + dot_list[right_index])/2 + change))))
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
        white = (220, 220, 220)
        for i in range(0, 8):
            pygame.draw.circle(surface, self.color, (self.pos_x + self.x_list[i], 720-self.y_list[i]), self.r_list[i], 0)
