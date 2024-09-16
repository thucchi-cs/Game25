# Libraries imports
import pygame

# Person sprite
class Person(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pic, x, y):
        super().__init__()
        # Load image and position
        self.image = pygame.image.load('graphics/' + pic)
        self.image = pygame.transform.scale(self.image, (100,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    # Move sprite with arrow keys
    def move_arrows(self, key):
        self.rect.y -= 10 if (key[pygame.K_UP]) else 0
        self.rect.y += 10 if (key[pygame.K_DOWN]) else 0
        self.rect.x -= 10 if (key[pygame.K_LEFT]) else 0
        self.rect.x += 10 if (key[pygame.K_RIGHT]) else 0
    
    # Move sprite with wasd keys
    def move_wasd(self, key):
        self.rect.y -= 10 if (key[pygame.K_w]) else 0
        self.rect.y += 10 if (key[pygame.K_s]) else 0
        self.rect.x -= 10 if (key[pygame.K_a]) else 0
        self.rect.x += 10 if (key[pygame.K_d]) else 0