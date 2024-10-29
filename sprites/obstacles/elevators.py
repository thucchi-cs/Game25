import pygame

class Elevators(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pos, size, flipped, y2):
        super().__init__()
        # Load image
        self.image = pygame.image.load("graphics/elevator.png")
        self.image = pygame.transform.scale(self.image, size)
        self.image = pygame.transform.flip(self.image, flip_x= flipped, flip_y= False)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.y = pos[0], pos[1]
        
        # Moving varibles
        self.dest = y2
        self.speed = 3 if (self.dest > self.rect.y) else -3
        self.clearing = False
        self.appearing = False

    # Move to destination
    def animation(self):
        if abs(self.rect.y - self.dest) > 3:
            self.rect.y += self.speed
        else:
            self.moving = False

    # Update - periodic
    def update(self):
        if self.clearing:
            self.animation()

    # Scroll with screen
    def scroll(self, direction,speed):
        if direction == 'D':
            self.rect.y +=speed 
        elif direction == 'U':
            self.rect.y+=speed
