# Libraries imports
import pygame
import random, math

# Person sprite
class Person(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pic, x, y):
        super().__init__()
        # Load image and position
        self.image_path = 'graphics/' + pic
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (25,50))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        
        # Rotation variable
        self.angle = 0
        self.rotation_spd = 10

        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 5
    
    # Move sprite with arrow keys
    def move_arrows(self, key, wall):
        
            # Movement
            if key[pygame.K_UP]:
                rise = math.sin(math.radians(self.angle)) * self.speed
                run = math.cos(math.radians(self.angle)) * self.speed
                self.rect.centerx += int(run)
                self.rect.centery -= int(rise)

                if pygame.sprite.collide_mask(wall, self):
                     self.rect.centerx -= int(run)
                     self.rect.centery += int(rise)

            # Rotation
            if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
                x, y = self.rect.centerx, self.rect.centery
                rotation = self.rotation_spd if key[pygame.K_LEFT] else -self.rotation_spd
                self.angle += rotation
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.smoothscale(self.image, (25,50))
                self.image = pygame.transform.rotate(self.image, self.angle-90)
                self.rect = self.image.get_rect(center=(x, y))

                if pygame.sprite.collide_mask(wall, self):
                    self.angle -= rotation
                    self.image = pygame.image.load(self.image_path).convert_alpha()
                    self.image = pygame.transform.smoothscale(self.image, (25,50))
                    self.image = pygame.transform.rotate(self.image, self.angle-90)
                    self.rect = self.image.get_rect(center=(x, y))

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