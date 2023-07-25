import pygame
import numpy
from utils.config import Sim

_C = Sim.conf

class Trail:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def update(self, ant):
        pixel_array = pygame.surfarray.pixels3d(self.surface)
        alpha_array = pygame.surfarray.pixels_alpha(self.surface)
        x = int(ant.rect.x)
        y = int(ant.rect.y)
        if ant.has_food:
            pixel_array[x, y] = (0, (max(int(255*1.2), 255)), 0)  # Green color
        else:
            pixel_array[x, y] = _C("colors", "CYAN")  # Green color
        alpha_array[x, y] = 255  # Full opacity

    def decay(self):
        alpha_array = pygame.surfarray.pixels_alpha(self.surface)
        alpha_array[alpha_array > 0] -= int(_C("trail", "DECAY_RATE"))
        low_alpha = alpha_array < 50
        alpha_array[low_alpha] = 0

        #pixel_array = pygame.surfarray.pixels3d(self.surface)
        #pixel_array[low_alpha] = [0, 0, 0]  # Set color to black when alpha is lower than 10

    def draw(self, window):
        window.blit(self.surface, (0, 0)) 
