import pygame
from .colors import Color


class Window:
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 500
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Lab 1.05")
        self.run = True
        self.loop()

    def loop(self) -> bool:
        pygame.draw.rect(self.screen, Color.WHITE.value, (0, 0, self.WIDTH, self.HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                return False
        return True

    @staticmethod
    def update():
        pygame.display.update()