# Libraries imports
import pygame
import math


# Person sprite
class Flies(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y, keys):
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

        # Keys for movements
        self.up_key = keys[0]
        self.down_key = keys[1]
        self.left_key = keys[2]
        self.right_key = keys[3]

    
    # Move sprite with arrow keys
    def move_arrows(self, key, walls):
        
        # Move Forward
        if (key[self.up_key] or key[self.down_key]):
            # Move
            rise = math.sin(math.radians(self.angle)) * self.speed
            run = math.cos(math.radians(self.angle)) * self.speed
            self.rect.centerx += int(run) if key[self.up_key] else -int(run)
            self.rect.centery -= int(rise) if key[self.up_key] else -int(rise)

            # Prevent moving into walls
            for wall in walls:
                if pygame.sprite.collide_mask(wall, self):
                    self.rect.centerx -= int(run) if key[self.up_key] else -int(run)
                    self.rect.centery += int(rise) if key[self.up_key] else -int(rise)

            # Off Screen Movement 
            if (self.rect.y < 0) or (self.rect.y > (600 - self.rect.height)):
                for wall in walls:
                    self.rect.y = (600-self.rect.height) if (self.rect.y > 500) else 0
                    wall.wall_move('U' if (self.rect.y < 100) else 'D')

            # Stay in screen
            if (self.rect.x < 0) or (self.rect.x > (500 - self.rect.width)):
                self.rect.centerx -= int(run) if key[self.up_key] else -int(run)
                self.rect.centery += int(rise) if key[self.up_key] else -int(rise)
                

        # Rotate
        if key[self.left_key] or key[self.right_key]:
            
            # Calculate rotation
            rotation = self.rotation_spd if key[self.left_key] else -self.rotation_spd
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
            
    # Check collision with lasers
    def check_lasers(self, lasers):
        for laser in lasers:
            if not not pygame.sprite.collide_mask(self, laser):
                return True
        return False