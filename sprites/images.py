import pygame
import constants
# Button for menu
class imgDisplay(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos, img,n=None):
        super().__init__()
        # Load image and rect
        self.image = pygame.image.load(f'graphics/{img}')
        self.size = size
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.n = n
        self.image_paths = [f'graphics/fly'+str(self.n)+'.1.png', f'graphics/fly'+str(self.n)+'.2.png']
        self.current_image = self.image_paths[0]
        self.counter = 0
    def move_up(self):
        self.rect.y += constants.SPEED
    def animate_fly(self):
        self.counter += 1
        if self.counter % 5 == 0:
            current = self.image_paths.index(self.current_image)
            current = 1 - current
            self.current_image = self.image_paths[current]
        self.image = pygame.image.load(self.current_image)
        self.image = pygame.transform.scale(self.image, self.size)

            



