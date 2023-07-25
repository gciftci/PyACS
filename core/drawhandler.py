import pygame

from utils.config import Sim

_C = Sim.conf

class DrawHandler:
    def __init__(self):
        pass

    def draw(self):
        self.timer_draw += self.clock.get_time()
        
        # Clear Surface
        self.main_surface.fill((255, 255, 255))

        # Draw Objects
        # Trail
        if self.timer_draw >= _C("render", "DRAW_TIME"):
            self.trail.draw(self.main_surface)
            self.trail_food.draw(self.main_surface)
            self.timer_draw = 0
        # Nest
        self.nest.draw(self.main_surface)
        # Food
        for food in self.foods:
            food.draw(self.main_surface)
        # Ants
        for ant in self.ants:
            ant.draw(self.main_surface)

        # UI (Text)
        self.text_update += self.clock.get_time()
        self.text.draw(self.main_surface, self.clock, self.ants)
        self.text_update = 0

        # Update
        pygame.display.update()