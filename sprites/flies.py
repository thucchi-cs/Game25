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
        self.actualX = 0
        self.actualy = 0
        self.realX = self.rect.centerx + self.actualX
        self.realY = self.rect.centery + self.actualy
        self.rise = 0.00
        self.run = 0.00

        
        # Movements variables
        self.angle = 0
        self.rotation_spd = 10
        self.speed = 5

    
    # Move sprite with arrow keys
    def move_arrows(self, key, walls,rocks):
        
        # Move Forward
        if (key[pygame.K_UP] or key[pygame.K_DOWN]):
            # Move
            self.rise = math.sin(math.radians(self.angle)) * self.speed
            self.run = math.cos(math.radians(self.angle)) * self.speed
            self.rect.centerx += int(self.run) if key[pygame.K_UP] else -int(self.run)
            self.rect.centery -= int(self.rise) if key[pygame.K_UP] else -int(self.rise)

            # Prevent moving into walls
            for wall in walls:
                if pygame.sprite.collide_mask(wall, self):
                    self.rect.centerx -= int(self.run) if key[pygame.K_UP] else -int(self.run)
                    self.rect.centery += int(self.rise) if key[pygame.K_UP] else -int(self.rise)


            # Off Screen Movement 
            if (self.rect.y < 0) or (self.rect.y > (600 - self.rect.height)):
                if self.rect.y < 0:
                    self.actualy += -int(self.rise)
                elif self.rect.y > (600-self.rect.height):
                    self.actualy += -int(self.rise)


                for wall in walls:
                    self.rect.y = (600-self.rect.height) if (self.rect.y > 500) else 0
                    wall.wall_move('U' if (self.rect.y < 100) else 'D',int(self.rise))


                for rock in rocks:
                    self.rect.y = (600-self.rect.height) if (self.rect.y > 500) else 0
                    rock.rock_move('U' if (self.rect.y < 100) else 'D',int(self.rise))
            self.realX = self.rect.centerx + self.actualX
            self.realY = self.rect.centery + self.actualy
    
                                        


                

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
            
    def collide_rock(self,rocks):
        for rock in rocks:
            if pygame.sprite.collide_mask(rock,self):
                return 'dead'
            else:
                return 'alive'

    # Move sprite with wasd keys
    def move_wasd(self, key, walls):
        # Move Forward
        if key[pygame.K_w] or key[pygame.K_s]:
            # Move
            self.rise = math.sin(math.radians(self.angle)) * self.speed
            self.run = math.cos(math.radians(self.angle)) * self.speed
            self.rect.centerx += int(self.run) if key[pygame.K_w] else -int(self.run)
            self.rect.centery -= int(self.rise) if key[pygame.K_w] else -int(self.rise)

            # Prevent moving into walls
            for wall in walls:
                if pygame.sprite.collide_mask(wall, self):
                    self.rect.centerx -= int(self.run) if key[pygame.K_w] else -int(self.run)
                    self.rect.centery += int(self.rise) if key[pygame.K_w] else -int(self.rise)

            # Off Screen Movement 
            if (self.rect.x < 0) or (self.rect.x > (1000 - self.rect.width)):
                for wall in walls:
                    self.rect.x = (1000-self.rect.width) if (self.rect.x > 900) else 0
                    wall.wall_move('R' if (self.rect.x < 10) else 'L')
                

        # Rotate
        if key[pygame.K_a] or key[pygame.K_d]:
            
            # Calculate rotation
            rotation = self.rotation_spd if key[pygame.K_a] else -self.rotation_spd
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

    # Move with 1 and 2
    def move1(self, key):
        self.rect.x -= self.speed if (key[pygame.K_1]) else 0
        self.rect.x += self.speed if (key[pygame.K_2]) else 0
    
    # Move with 9 and 0
    def move2(self, key):
        self.rect.x -= self.speed if (key[pygame.K_9]) else 0
        self.rect.x += self.speed if (key[pygame.K_0]) else 0