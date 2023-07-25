import pygame

from utils.config import Sim
_C = Sim.conf

class Text:
    def __init__(self):
        self.passed = 0
        self.fps = 0
        self.f16 = pygame.font.Font(None, 16)
        self.f20 = pygame.font.Font(None, 20)
        self.f32 = pygame.font.Font(None, 32)

    def get_text_width(self, text, font):
        text_surface = font.render(text, True, _C("colors", "BLACK"))
        return text_surface.get_width()

    def draw_text(self, surface, text, pos, font):
        text_surface = font.render(text, True, _C("colors", "BLACK"))
        surface.blit(text_surface, pos)

    def draw_fps(self, surface, clock):
        self.passed += clock.get_time()
        
        if self.passed > 500:
            self.fps = int(clock.get_fps())
            self.passed = 0
        self.draw_text(surface, f"FPS: {self.fps}", (10, 10), self.f32)

    def draw_count(self, surface, ants):
        ant_count_text = f"Ants: {len(ants)}"
        self.draw_text(surface, ant_count_text, (_C("WIDTH") - self.get_text_width(ant_count_text, self.f16) - 10, 10), self.f16)

    """ def draw_stats(self, surface, ants_w_food):
        ant_food_text = f'Food: {ants_w_food} // No-Food: {_C("ant","AMOUNT")-ants_w_food}'
        self.draw_text(surface, ant_food_text, (_C("WIDTH") - self.get_text_width(ant_food_text, self.f16) - 10, _C("HEIGHT")-20), self.f16)
 """
    def draw(self, surface, clock, ants):
        self.draw_fps(surface, clock)
        self.draw_count(surface, ants)