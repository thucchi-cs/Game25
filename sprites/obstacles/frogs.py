import pygame
import constants

class Frog(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pos, flip, wait_time):
        super().__init__()
        # Load image and position
        self.size = (220,50)
        self.flip = flip
        self.pos = pos
        self.index = 1
        self.image_path = 'graphics/frog'+str(self.index)+'.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)
        self.image = pygame.transform.flip(self.image, flip, False)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.bottom = pos[1]
        self.counter = 0
        self.wait = 0
        self.wait_time = wait_time * 40

    def update(self):
        if self.wait == 0:
            self.animate()

        if self.index == 8 or self.index == 1:
            self.wait += 1
            if ((self.wait >= self.wait_time) and self.index == 1) or ((self.wait >= 20) and self.index == 8):
                self.wait = 0
        
    
    def animate(self):
        self.counter += 1
        if self.counter % 3 == 0:
            # print(self.index)
            self.index += 1
            if self.index == 7 or self.index == 6:
                self.index = 8
            self.index %= 11
            self.image_path = 'graphics/frog'+str(self.index)+'.png'
            self.image = pygame.image.load(self.image_path)
            self.image = pygame.transform.scale(self.image, self.size)
            self.image = pygame.transform.flip(self.image, self.flip, False)
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.bottom = self.pos[1]
    
    # Scroll with screen
    def scroll(self, addition):
        self.rect.y += constants.SPEED + addition
        self.pos = (self.pos[0], self.pos[1] + constants.SPEED)