from OpenGL.GL import *
from CC3501Utils import *

class Vista:
    def dibujar(self, pjs, surface):

        for p in pjs:
            p.dibujar(surface)