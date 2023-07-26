import pygame
import random

from utils.text import Text
from utils.config import Sim

from core.ehandler import EHandler
from core.drawhandler import DrawHandler
from core.updatehandler import UpdateHandler

from core.objects.nest import Nest
from core.objects.food import Food
from core.objects.ant import Ant
from core.objects.trail import Trail


_C = Sim.conf

class Simulation:
    def __init__(self):
        # General
        pygame.init()
        self.main_surface = pygame.display.set_mode((_C("WIDTH"), _C("HEIGHT")), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.timer_draw = 0
        self.timer_update = 0
        self.text_update = 0
        self.running = True

        # Objects
        self.nest = Nest(_C("WIDTH") // 2, _C("HEIGHT") // 2)
        self.ants = [Ant(_C("WIDTH") // 2, _C("HEIGHT") // 2) for _ in range(_C("ant", "AMOUNT"))]
        self.foods = [Food(random.uniform(0, _C("WIDTH")), random.uniform(0, _C("HEIGHT"))) for _ in range(_C("food", "AMOUNT"))]
        self.trail = Trail(_C("WIDTH"), _C("HEIGHT"))
        self.trail_food = Trail(_C("WIDTH"), _C("HEIGHT"))

        # UI
        self.text = Text()

    def run(self):
        while self.running:
            EHandler.event_handler(self)
            UpdateHandler.update(self)
            DrawHandler.draw(self)

            self.clock.tick(60)
        pygame.quit()

''' main.py '''
if __name__ == '__main__':
    sim = Simulation()
    sim.run()