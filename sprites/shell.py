import pygame
import globals

class Collide_Box(pygame.sprite.Sprite):
        def __init__(self, rect, width):
            super().__init__()
            self.shell = width
            self.rect = pygame.Rect(rect.x - self.shell, rect.y - self.shell, rect.width + 2*self.shell, rect.height + 2*self.shell)
        def update(self, rect):
            self.rect = pygame.Rect(rect.x - self.shell, rect.y - self.shell, rect.width + 2*self.shell, rect.height + 2*self.shell)
            # pygame.draw.rect(constants.SCREEN, (255,255,255), self.rect, 1)