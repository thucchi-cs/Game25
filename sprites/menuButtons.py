import pygame
import math

# Button for menu
class menuBtn(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos, img):
        super().__init__()
        # Load image and rect
        self.image = pygame.image.load(f'graphics/menu_buttons/{img}')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 10
        self.scaleFactor = 1.1
        self.image_path = f'graphics/menu_buttons/{img}'
        self.w = size[0]
        self.h = size[1]
        self.pos = pos

    # Check if is being clicked by mouse
    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
    
    def glide_to(self, pos):
        if (((self.rect.centerx - pos[0])**2) + ((self.rect.centery - pos[1])**2))**0.5 > 10:
            glide_y = pos[1] - self.rect.centery
            glide_x = pos[0] - self.rect.centerx
            glide_angle = math.atan2(glide_y,glide_x)
            self.angle = 90 + math.degrees(glide_angle)
            self.rect.centerx += (math.cos(glide_angle) * self.speed)
            self.rect.centery += (math.sin(glide_angle) * self.speed)
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