import pygame

class Elevator(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y, size, flipped, y2):
        super().__init__()
        # Load image
        self.image = pygame.image.load("graphics/elevator.png")
        self.image = pygame.transform.scale(self.image, size)
        self.image = pygame.transform.flip(self.image, flip_x= flipped, flip_y= False)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.y = x, y
        
        # Moving varibles
        self.dest = y2
        self.speed = 3 if (self.dest > self.rect.y) else -3
        self.moving = False

    # Move to destination
    def remove(self):
        if abs(self.rect.y - self.dest) > 3:
            self.rect.y += self.speed
        else:
            self.moving = False

    # Update animation
    def update(self):
        if self.moving:
            self.remove()