import pygame
import constants
# Pause
class Pause(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        super().__init__()
        # Load image and rect
        self.image = pygame.image.load(f'graphics/menu_buttons/blue_pause.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 15
