import pygame

class Lasers(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y, n, size, angle):
        super().__init__()
        # Load image
        self.image_path = 'graphics/laser' + str(n) + '.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.y = x, y
        self.originalX = x

        # Animation variables
        self.counter = 0
        self.clearing = False
        self.appearing = False
        self.show = True
        
    # Blink animation
    def animation(self):
        self.show = not ((self.counter % 8 >= 0) and (self.counter % 8 <= 2))
        self.counter += 1
        if self.counter > 25:
            self.counter = 0
            self.show = self.appearing
            self.clearing = False
            self.appearing = False

    # Animation
    def update(self):
        if self.clearing or self.appearing:
            self.animation()

        self.rect.centerx = self.originalX if self.show else (601 + self.rect.width)