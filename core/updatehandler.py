import pygame
from utils.config import Sim

from core.objects.ant import Ant

_C = Sim.conf
class UpdateHandler:
    def __init__(self) -> None:
        pass

    def update(self):
        self.timer_update += self.clock.get_time()
        if self.timer_update >= 50:
            for ant in self.ants:
                ant.move(self.foods, self.nest)
                if ant.has_food:
                    self.trail_food.update(ant)
                else:
                    self.trail.update(ant)

        if self.timer_update >= _C("render", "UPDATE_TIME"):
            self.trail.decay()
            self.trail_food.decay()
            self.timer_update = 0
        if self.timer_update >= 200:
            if self.clock.get_fps() > 55:
                for _ in range(20):
                    self.ants.append(Ant(_C("WIDTH") // 2, _C("HEIGHT") // 2))
            elif self.clock.get_fps() < 55:
                if len(self.ants) > 0:
                    self.ants.pop()
        #print(self.timer)