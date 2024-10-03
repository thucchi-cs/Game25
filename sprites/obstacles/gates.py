import pygame

class Gate(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos, direction):
        super().__init__()
        self.direction = direction
        self.size = size
        self.pos = pos
        # Image path variables
        self.image_path = 'graphics/gates/gate1.png'
        self.path_index = 0
        self.image_paths = [f'graphics/gates/gate{i}.png' for i in range(1,19)]
        # Image rendering
        self.image = pygame.image.load(self.image_path)
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        self.height = int(size / aspect_ratio)
        self.image = pygame.transform.smoothscale(self.image, (size,self.height))
        # Rotation based off direction
        rotation = 90 * direction
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect(topleft=pos)
        # Open and closed variables
        self.open = False
        self.closed = True

    
    def unlock(self):
        if self.path_index < 17:
            # Move forward one in the list of image paths
            self.path_index += 1
            self.image_path = self.image_paths[self.path_index]
            # Render new image
            self.image = pygame.image.load(self.image_path)
            original_width, original_height = self.image.get_size()
            aspect_ratio = original_width / original_height
            self.height = int(self.size / aspect_ratio)
            self.image = pygame.transform.smoothscale(self.image, (self.size,self.height))
            # Rotation based off direction
            rotation = 90 * self.direction
            self.image = pygame.transform.rotate(self.image, rotation)
            self.rect = self.image.get_rect(topleft=self.pos)
            self.open = True if self.path_index == 17 else False
            self.closed = True if self.path_index == 0 else False

    
    def lock(self):
        if self.path_index > 0:
            # Move back one in the list of image paths
            self.path_index -= 1
            self.image_path = self.image_paths[self.path_index]
            # Render new image
            self.image = pygame.image.load(self.image_path)
            original_width, original_height = self.image.get_size()
            aspect_ratio = original_width / original_height
            self.height = int(self.size / aspect_ratio)
            self.image = pygame.transform.smoothscale(self.image, (self.size,self.height))
            # Rotation based off direction
            rotation = 90 * self.direction
            self.image = pygame.transform.rotate(self.image, rotation)
            self.rect = self.image.get_rect(topleft=self.pos)
            self.closed = True if self.path_index == 0 else False
            self.open = True if self.path_index == 17 else False
