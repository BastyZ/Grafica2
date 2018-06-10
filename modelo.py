import random
import math
from CC3501Utils import *


def generate_mountain(dot_list, left_index, right_index, distance):
    roughness = .44
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

    def draw(self, surface):
        for i in range(0, self.ancho):
            pygame.draw.line(surface, (121, 85, 61), (i, 0), (i, self.dots[i]))
