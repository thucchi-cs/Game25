import pygame

class Buttons(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y, obstacle):
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
        self.obstacle = obstacle
        

    # When pressed
    def press(self, lasers, elevators, waters, gates):
        # Change image
        x, y = self.rect.centerx, self.rect.centery
        self.image_path = 'graphics/button-pressed.png' if self.image_path ==  'graphics/button.png' else  'graphics/button.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
        self.pressed = not self.pressed

        # Remove/add obstacle
        self.obstacle.clearing = self.pressed
        self.obstacle.appearing = not self.pressed

        # Return state of button
        return self.pressed



