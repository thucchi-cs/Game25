import pygame
import constants
import math

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
        self.speed = 10
        self.scaleFactor = 1.1
        self.image_path = f"graphics/{img}"
        self.w = size[0]
        self.h = size[1]
        self.pos = (pos[0] + self.w // 2, pos[1] + self.h//2)
        print(pos)
        print(self.pos)
        
    def scroll(self, addition):
        self.rect.y += constants.SPEED + addition 
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

    def glide_to(self, pos):
        if (((self.rect.x - pos[0])**2) + ((self.rect.y - pos[1])**2))**0.5 > 10:
            glide_y = pos[1] - self.rect.y
            glide_x = pos[0] - self.rect.x
            glide_angle = math.atan2(glide_y,glide_x)
            self.angle = 90 + math.degrees(glide_angle)
            self.rect.x += (math.cos(glide_angle) * self.speed)
            self.rect.y += (math.sin(glide_angle) * self.speed)
            return False
        return True
    
    def set_center(self, size, pos):
        self.pos = (pos[0] + size[0] // 2, pos[1] + size[1]//2)
    
    def zoomIn(self, size):
        if self.rect.width < size[0]:
            self.image = pygame.image.load(self.image_path)
            self.w *= self.scaleFactor
            self.h *= self.scaleFactor
            self.image = pygame.transform.scale(self.image, (self.w, self.h))
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            return True
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        return False



