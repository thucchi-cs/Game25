# Libraries imports
import pygame
import math


# Person sprite
class Flies(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y):
        super().__init__()
        # Load image and position
        self.image_path = 'graphics/fly.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (25,50))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        # Movements variables
        self.angle = 0
        self.rotation_spd = 10
        self.speed = 5

    
    # Move sprite with arrow keys
    def move_arrows(self, key, walls):
        
        # Move Forward
        if key[pygame.K_UP]:
            # Move only within screen
            if (self.rect.x > 0) and (self.rect.x < (1000 - self.rect.width)):
                # Move
                rise = math.sin(math.radians(self.angle)) * self.speed
                run = math.cos(math.radians(self.angle)) * self.speed
                self.rect.centerx += int(run)
                self.rect.centery -= int(rise)

                # Prevent moving into walls
                for wall in walls:
                    if pygame.sprite.collide_mask(wall, self):
                        self.rect.centerx -= int(run)
                        self.rect.centery += int(rise)

            # Off Screen Movement 
            else:
                for wall in walls:
                    self.rect.x += 2 if (self.rect.x < 10) else -2
                    wall.wall_move('R' if (self.rect.x < 10) else 'L')
                

        # Rotate
        if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
            
            # Calculate rotation
            rotation = self.rotation_spd if key[pygame.K_LEFT] else -self.rotation_spd
            self.angle += rotation

            # Render image
            x, y = self.rect.centerx, self.rect.centery
            self.image = pygame.image.load(self.image_path).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (25,50))
            self.image = pygame.transform.rotate(self.image, self.angle-90)
            self.rect = self.image.get_rect(center=(x, y))

            # Prevent moving into walls
            for wall in walls:
                if pygame.sprite.collide_mask(wall, self):
                    self.angle -= rotation
                    self.image = pygame.image.load(self.image_path).convert_alpha()
                    self.image = pygame.transform.smoothscale(self.image, (25,50))
                    self.image = pygame.transform.rotate(self.image, self.angle-90)
                    self.rect = self.image.get_rect(center=(x, y))
            

    # Move sprite with wasd keys
    def move_wasd(self, key):
        self.rect.y -= self.speed if (key[pygame.K_w]) else 0
        self.rect.y += self.speed if (key[pygame.K_s]) else 0
        self.rect.x -= self.speed if (key[pygame.K_a]) else 0
        self.rect.x += self.speed if (key[pygame.K_d]) else 0

    # Move with 1 and 2
    def move1(self, key):
        self.rect.x -= self.speed if (key[pygame.K_1]) else 0
        self.rect.x += self.speed if (key[pygame.K_2]) else 0
    
    # Move with 9 and 0
    def move2(self, key):
        self.rect.x -= self.speed if (key[pygame.K_9]) else 0
        self.rect.x += self.speed if (key[pygame.K_0]) else 0