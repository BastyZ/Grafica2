from CC3501Utils import *


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
        return dot_list
