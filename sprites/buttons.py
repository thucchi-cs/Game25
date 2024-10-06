import pygame

class Buttons(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y):
        super().__init__()
        # Load image
        self.size = (50, 25)
        self.image_path = 'graphics/button.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.pressed = False
        

    # When pressed
    def press(self, lasers, elevators):
        # Change image
        x, y = self.rect.centerx, self.rect.centery
        self.image_path = 'graphics/button-pressed.png' if self.image_path ==  'graphics/button.png' else  'graphics/button.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
        self.pressed = not self.pressed

        # Remove obstacle
        for laser in lasers:
            laser.blinking = True

        # Move elevator
        for elevator in elevators:
            elevator.moving = True
        
        # Return state of button
        self.pressed = not self.pressed
        return self.pressed



