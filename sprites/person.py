# Libraries imports
import pygame
import random

# Person sprite
class Person(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pic, x, y):
        super().__init__()
        # Load image and position
        self.image = pygame.image.load('graphics/' + pic)
        self.image = pygame.transform.scale(self.image, (25,50))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
    
    # Move sprite with arrow keys
    def move_arrows(self, key, wall):
        self.rect.y -= 10 if (key[pygame.K_UP]) else 0
        self.rect.y += 10 if (key[pygame.K_DOWN]) else 0
        self.rect.x -= 10 if (key[pygame.K_LEFT]) else 0
        self.rect.x += 10 if (key[pygame.K_RIGHT]) else 0
            
    def check_collision(self, coor1):
        return ((self.rect.right > coor1[0][0]) and (self.rect.x < coor1[0][1]) and (self.rect.bottom > coor1[0][0]) and (self.rect.y < coor1[0][1]))

    def within(self, point, range_):
        return (point in range(range_[0], range_[1]))
    
    def range_within(self, range1, range2):
        return len(set(i for i in (list(range1) + list(range2)) if (list(range1) + list(range2)).count(i) > 1)) > 0

    # Move sprite with wasd keys
    def move_wasd(self, key):
        self.rect.y -= 10 if (key[pygame.K_w]) else 0
        self.rect.y += 10 if (key[pygame.K_s]) else 0
        self.rect.x -= 10 if (key[pygame.K_a]) else 0
        self.rect.x += 10 if (key[pygame.K_d]) else 0

    def move1(self, key):
        self.rect.x -= 10 if (key[pygame.K_1]) else 0
        self.rect.x += 10 if (key[pygame.K_2]) else 0
    
    def move2(self, key):
        self.rect.x -= 10 if (key[pygame.K_9]) else 0
        self.rect.x += 10 if (key[pygame.K_0]) else 0