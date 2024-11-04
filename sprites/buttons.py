import pygame
import constants

class Buttons(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pos, obstacle):
        super().__init__()
        # Load image
        self.size = (50, 25)
        self.image_path = 'graphics/button.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.pressed = False
        self.obstacle = obstacle  
        

    # When pressed
    def press(self):
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

    # Scroll with screen
    def scroll(self):
        self.rect.y += constants.SPEED

