import pygame

from core.objects.ant import Ant

class EHandler:
    def __init__(self) -> None:
        pass

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if event.button == 1:  # Left click
                    # Create 10 ants at the click position
                    for _ in range(10):
                        self.ants.append(Ant(x, y))
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if event.button == 4:  # Scroll up
                    for _ in range(100):
                        self.ants.append(Ant(x, y))
                elif event.button == 5:  # Scroll down
                    if len(self.ants) > 100:
                        for _ in range(100):
                            self.ants.pop()