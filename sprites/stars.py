import pygame
import constants

class Stars(pygame.sprite.Sprite):
    def __init__(self, pos, id):
        super().__init__()
        self.image = pygame.image.load('graphics/star.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # ID represents whcih star it is (1, 2, or 3)
        self.id = id
    

    # Scroll with screen
    def scroll(self, addition):
        self.rect.y += constants.SPEED + addition