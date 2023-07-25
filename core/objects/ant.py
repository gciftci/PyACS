import pygame
import random
import math

from utils.config import Sim
_C = Sim.conf

class Ant:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, _C("ant", "SIZE"), _C("ant", "SIZE"))
        self.angle = random.uniform(0, 2 * math.pi)
        self.has_food = False
        self.switched_food = False
        self.switched_nest = False
        self.goto_nest = False
        self.angle_to_nest = 0
        self.goto_food = False
        self.angle_to_food = 0

    def move(self, foods, nest):
        """         if not self.has_food and not self.nearest_food:
            self.nearest_food = self.check_food(foods)
        if self.nearest_food and not self.has_food:
            dx = self.nearest_food.x - self.rect.x
            dy = self.nearest_food.y - self.rect.y
            angle_to_food = math.atan2(dy, dx)
            self.angle = angle_to_food """

        # Some wankiness in movement
        offset = random.uniform(-0.05, 0.05)
        self.angle += offset

        # Calculate new x, y based on the (potentially modified) angle
        dx = math.cos(self.angle) * (_C("ant", "SPEED") * random.uniform(0, 1 * math.pi))
        dy = math.sin(self.angle) * (_C("ant", "SPEED") * random.uniform(0, 1 * math.pi))

        # Update position
        self.rect.x += dx
        self.rect.y += dy

        self.check_boundaries()
        if not self.has_food:
            if not self.switched_nest:
                self.angle = -self.angle
                self.angle = math.pi - self.angle
                self.switched_nest = True
                self.switched_food = False
            if self.goto_food:
                self.angle = self.angle_to_food
            self.check_food(foods)
                
        elif self.has_food:
            if not self.switched_food:
                self.angle = -self.angle
                self.angle = math.pi - self.angle
                self.switched_food = True
                self.switched_nest = False
            if self.goto_nest:
                self.angle = self.angle_to_nest
            self.check_nest(nest)

        # Recalculate dx and dy after potentially flipping the angle
        self.rect.x = min(max(self.rect.x, 0), _C("WIDTH") - _C("ant", "SIZE"))
        self.rect.y = min(max(self.rect.y, 0), _C("HEIGHT") - _C("ant", "SIZE"))

    def check_boundaries(self):
        # Check boundaries (_C("WIDTH"), _C("HEIGHT"))
        if not (0 <= self.rect.x < _C("WIDTH") - _C("ant", "SIZE")):
            self.angle = math.pi - self.angle
        if not (0 <= self.rect.y < _C("HEIGHT") - _C("ant", "SIZE")):
            self.angle = -self.angle

    def check_food(self, foods):
        for food in foods:
            dx = food.x - self.rect.x
            dy = food.y - self.rect.y
            distance = math.sqrt(dx ** 2 + dy ** 2) - _C("food", "RADIUS") - _C("ant", "SIZE")
            if distance <= 50:
                self.goto_food = True
                self.angle_to_food = math.atan2(dy, dx)
            if distance <= 0:
                self.has_food = True
    
    def check_nest(self, nest):
        dx = nest.x - self.rect.x
        dy = nest.y - self.rect.y
        distance = math.sqrt(dx ** 2 + dy ** 2) - _C("food", "RADIUS") - _C("ant", "SIZE")
        if distance <= 250:
            self.goto_nest = True
            self.angle_to_nest = math.atan2(dy, dx)
        if distance <= 0:
            self.has_food = False

    def draw(self, window):
        pygame.draw.rect(window, _C("colors", "BLUE"), self.rect)
