import pygame

class Web(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos):
        super().__init__()
        # Load image and position
        self.size = size
        self.image_path = 'graphics/web.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect(center=pos)