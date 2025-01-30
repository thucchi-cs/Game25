import pygame
import constants

class End(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,pos,scale):
        super().__init__()
        # Load image
        self.image = pygame.image.load("graphics/yayyy.png")
        self.image = pygame.transform.smoothscale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def scroll(self):
        self.rect.y += constants.SPEED
    