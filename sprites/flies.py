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
        self.size = (12, 24)
        self.image = pygame.transform.scale(self.image, self.size)
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        # Positioning
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

        # Stuck variable restricts movement when in web
        self.stuck = False

        # Keys for movements
        self.up_key = keys[0]
        self.down_key = keys[1]
        self.left_key = keys[2]
        self.right_key = keys[3]

    
    # Move sprite with arrow keys
    def move_arrows(self, key, walls, gates, rocks, waters):
        if key[pygame.K_SPACE]:
            self.stuck = False
        if not self.stuck:
            # Move Forward
            if (key[self.up_key] or key[self.down_key]):
                # Move
                self.rise = math.sin(math.radians(self.angle)) * self.speed
                self.run = math.cos(math.radians(self.angle)) * self.speed
                self.rect.centerx += int(self.run) if key[self.up_key] else -int(self.run)
                self.rect.centery -= int(self.rise) if key[self.up_key] else -int(self.rise)

                # Prevent moving into walls and gates
                for object in pygame.sprite.Group(walls, waters, gates):
                    if pygame.sprite.collide_mask(object, self):
                        self.rect.centerx -= int(self.run) if key[self.up_key] else -int(self.run)
                        self.rect.centery += int(self.rise) if key[self.up_key] else -int(self.rise)

                # Off Screen Movement 
                if (self.rect.y < 0) or (self.rect.y > (600 - self.rect.height)):
                    if self.rect.y < 0:
                        self.actualy += -int(self.rise)
                    elif self.rect.y > (600-self.rect.height):
                        self.actualy += -int(self.rise)

                    self.rect.y = (600-self.rect.height) if (self.rect.y > 500) else 0

                # Adjust positions
                self.realX = self.rect.centerx + self.actualX
                self.realY = self.rect.centery + self.actualy

                # Stay in screen
                if (self.rect.x < 0) or (self.rect.x > (500 - self.rect.width)):
                    self.rect.centerx -= int(self.run) if key[self.up_key] else -int(self.run)
                    self.rect.centery += int(self.rise) if key[self.up_key] else -int(self.rise)
                    

            # Rotate
            if key[self.left_key] or key[self.right_key]:
                
                # Calculate rotation
                rotation = self.rotation_spd if key[self.left_key] else -self.rotation_spd
                self.angle += rotation

                # Render image
                x, y = self.rect.centerx, self.rect.centery
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.image = pygame.transform.smoothscale(self.image, self.size)
                self.image = pygame.transform.rotate(self.image, self.angle-90)
                self.rect = self.image.get_rect(center=(x, y))

                # Prevent moving into walls
                for object in pygame.sprite.Group(walls, waters, gates):
                    if pygame.sprite.collide_mask(object, self):
                        self.angle -= rotation
                        self.image = pygame.image.load(self.image_path).convert_alpha()
                        self.image = pygame.transform.smoothscale(self.image, self.size)
                        self.image = pygame.transform.rotate(self.image, self.angle-90)
                        self.rect = self.image.get_rect(center=(x, y))

    # Check if stuck in webs
    def check_web(self, webs):
        collided_web = pygame.sprite.spritecollideany(self, webs)
        if collided_web and math.dist(collided_web.rect.center, self.rect.center) <= (1/2)*collided_web.size:
            self.stuck = True
        else:
            self.stuck = False

    # Check for collision with rocks          
    def collide_rock(self, rocks):
        for rock in rocks:
            if pygame.sprite.collide_mask(rock, self):
                return True
        return False
            
    # Check collision with lasers
    def check_lasers(self, lasers):
        for laser in lasers:
            if pygame.sprite.collide_mask(self, laser):
                return True
        return False

    # Move with the elevator
    def elevator_move(self, elevators):
        for elevator in elevators:
            if (self.elevator_collide(elevator)) and (elevator.clearing) and (pygame.sprite.collide_mask(self, elevator)):
                self.rect.y += elevator.speed

    # Check if currently inside and touching a wall of elevator
    def elevator_collide(self, elevator):
        part = self.rect.width / 2
        return (self.rect.x > (elevator.rect.x - part)) and (self.rect.right < (elevator.rect.right + part)) and (self.rect.y > (elevator.rect.y + 1)) and (self.rect.bottom < (elevator.rect.bottom - 1))

    def check_btn(self, btn):
        return pygame.sprite.collide_mask(self, btn)