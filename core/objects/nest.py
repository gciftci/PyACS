import pygame

from utils.config import Sim

_C = Sim.conf


class Nest:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.circle(window, _C("colors", "BLACK"), (self.x, self.y), _C("nest", "RADIUS"))
