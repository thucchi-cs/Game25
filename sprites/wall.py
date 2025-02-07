import pygame
import constants

class Wall(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos):
        super().__init__()
        self.image = pygame.image.load('graphics/WALLLLLLLLLLL.png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.actualX = pos[0]
        self.actualY = pos[1]

    # Scroll with screen
    def scroll(self):
        self.rect.y += constants.SPEED
