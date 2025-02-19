import pygame
import globals

class Elevators(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pos, size, flipped, y2):
        super().__init__()
        # Load image
        self.image = pygame.image.load("graphics/newGraphics/Elevatorred.png")
        self.image = pygame.image.load("graphics/elevator.png")
        self.image = pygame.transform.scale(self.image, size)
        self.image = pygame.transform.flip(self.image, flip_x= flipped, flip_y= False)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.y = pos[0], pos[1]
        
        # Moving varibles
        self.dest = y2
        self.start = pos[1]
        dist = abs(self.start - self.dest)
        self.speed = dist // 50
        self.speed *= 1 if self.dest > self.rect.y else -1
        self.clearing = False
        self.appearing = False

    # Move to destination
    def animation(self):
        if ((abs(self.rect.y - self.dest) > 3) and self.clearing) or ((abs(self.rect.y - self.start) > 3) and self.appearing):
            # Move
            self.rect.y += self.speed if self.clearing else -self.speed
            
            # Avoid crushing a fly
            for fly in globals.players:
                if pygame.sprite.collide_mask(self, fly) and not fly.elevator_collide(self):
                    self.rect.y -= self.speed if self.clearing else -self.speed
                    
        else:
            self.clearing = False
            self.appearing = False

    # Update - periodic
    def update(self):
        if self.clearing or self.appearing:
            self.animation()

    # Scroll with screen
    def scroll(self, addition):
        self.rect.y += globals.SPEED + addition
        self.dest += globals.SPEED + addition
        self.start += globals.SPEED + addition
