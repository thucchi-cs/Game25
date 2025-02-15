import pygame
import pygame.image

class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, scale):
        super().__init__()
        self.image = pygame.image.load("graphics/cloud.png")
        self.image = pygame.transform.scale_by(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    def move(self):
        self.rect.x += 1
        if self.rect.x > 500:
            self.rect.x = -self.rect.width