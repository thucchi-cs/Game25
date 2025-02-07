import pygame
import constants

class Gate(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos, rotation):
        super().__init__()
        self.rotation = rotation
        self.size = size
        self.pos = pos
        # Image path variables
        self.image_path = 'graphics/newGraphics/RailRed1.png'
        self.path_index = 0
        self.image_paths = [f'graphics/newGraphics/RailRed{i}.png' for i in range(1,19)]
        # Image rendering
        self.image = pygame.image.load(self.image_path)
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        self.height = int(size / aspect_ratio)
        self.image = pygame.transform.smoothscale(self.image, (size,self.height))
        # Rotation based off direction
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect(topleft=pos)
        # Open and closed variables
        self.open = False
        self.closed = True
        self.clearing = False
        self.appearing = False
    
    # Animate opening and closing
    def animation(self):
        # Move forward or backwoards one in the list of image paths
        # Depending on if the gate is opening or closing
        self.path_index += 1 if self.clearing else -1
        self.image_path = self.image_paths[self.path_index]
        # Render new image
        self.image = pygame.image.load(self.image_path)
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        self.height = int(self.size / aspect_ratio)
        self.image = pygame.transform.smoothscale(self.image, (self.size,self.height))
        # Rotation based off direction
        self.image = pygame.transform.rotate(self.image, self.rotation)
        if self.path_index == 17 or self.path_index == 0:
            self.open = True if self.path_index == 17 else False
            self.closed = True if self.path_index == 0 else False
            self.clearing = False
            self.appearing = False
    
    # Update - periodic
    def update(self):
        # Animate if needed
        if self.clearing or self.appearing:
            self.animation()

    # Scroll with screen
    def scroll(self):
        self.rect.y += constants.SPEED