import pygame


class Window:
    def __init__(self):
        self.white = (255, 255, 255)

    def draw(self, screen):
        rect1 = pygame.Rect((100, 100), (100, 100))
        pygame.draw.rect(screen, self.white, rect1)
