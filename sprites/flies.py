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

        # Stuck variable restricts movement when in web
        self.stuck = False

    
    # Move sprite with arrow keys
    def move_arrows(self, key, walls, gates):
        
        # Move Forward
        if (key[pygame.K_UP] or key[pygame.K_DOWN]):
            # Move
            rise = math.sin(math.radians(self.angle)) * self.speed
            run = math.cos(math.radians(self.angle)) * self.speed
            self.rect.centerx += int(run) if key[pygame.K_UP] else -int(run)
            self.rect.centery -= int(rise) if key[pygame.K_UP] else -int(rise)

            # Prevent moving into walls and gates
            for wall in walls:
                if pygame.sprite.collide_mask(wall, self):
                    self.rect.centerx -= int(run) if key[pygame.K_UP] else -int(run)
                    self.rect.centery += int(rise) if key[pygame.K_UP] else -int(rise)
            for gate in gates:
                if pygame.sprite.collide_mask(gate, self):
                    self.rect.centerx -= int(run) if key[pygame.K_UP] else -int(run)
                    self.rect.centery += int(rise) if key[pygame.K_UP] else -int(rise)

            # Off Screen Movement 
            if (self.rect.y < 0) or (self.rect.y > (600 - self.rect.height)):
                for wall in walls:
                    self.rect.y = (600-self.rect.height) if (self.rect.y > 500) else 0
                    wall.wall_move('U' if (self.rect.y < 100) else 'D')
                

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
            for gate in gates:
                if pygame.sprite.collide_mask(gate, self):
                    self.angle -= rotation
                    self.image = pygame.image.load(self.image_path).convert_alpha()
                    self.image = pygame.transform.smoothscale(self.image, (25,50))
                    self.image = pygame.transform.rotate(self.image, self.angle-90)
                    self.rect = self.image.get_rect(center=(x, y))
            

    # Move sprite with wasd keys
    def move_wasd(self, key, walls, gates):
        # Move Forward
        if key[pygame.K_w] or key[pygame.K_s]:
            # Move
            rise = math.sin(math.radians(self.angle)) * self.speed
            run = math.cos(math.radians(self.angle)) * self.speed
            self.rect.centerx += int(run) if key[pygame.K_w] else -int(run)
            self.rect.centery -= int(rise) if key[pygame.K_w] else -int(rise)

            # Prevent moving into walls and gates
            for wall in walls:
                if pygame.sprite.collide_mask(wall, self):
                    self.rect.centerx -= int(run) if key[pygame.K_w] else -int(run)
                    self.rect.centery += int(rise) if key[pygame.K_w] else -int(rise)
            for gate in gates:
                if pygame.sprite.collide_mask(gate, self):
                    self.rect.centerx -= int(run) if key[pygame.K_w] else -int(run)
                    self.rect.centery += int(rise) if key[pygame.K_w] else -int(rise)

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
            for gate in gates:
                if pygame.sprite.collide_mask(gate, self):
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


    def check_web(self, webs):
        collided_web = pygame.sprite.spritecollideany(self, webs)
        if collided_web and math.dist(collided_web.rect.center, self.rect.center) <= (1/2)*collided_web.size:
            self.stuck = True