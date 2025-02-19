import pygame
import globals

class Window(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image_path = image
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (16,20))
        self.scaleFactor = 1.1
        self.rect = self.image.get_rect()
        self.rect.center = (250, 300)
        self.w = 16
        self.h = 20
        
    def zoomIn(self):
        if self.rect.width < 400:
            self.image = pygame.image.load(self.image_path)
            self.w *= self.scaleFactor
            self.h *= self.scaleFactor
            self.image = pygame.transform.scale(self.image, (self.w, self.h))
            self.rect = self.image.get_rect()
            self.rect.center = (250, 300)
            return True
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (250, 300)
        return False
    
    def draw(self):
        globals.SCREEN.blit(self.image, (self.rect.x, self.rect.y))