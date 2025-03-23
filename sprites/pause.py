import pygame
import constants
# Pause
class Pause(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        super().__init__()
        # Load image and rect
        self.image = pygame.image.load(f"graphics/dummy_do_2_I_hate_this_job_at_least_I_get_decent_pay_and_bonuses.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 15
