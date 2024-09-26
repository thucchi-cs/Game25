import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, size, pos,speed):
        super().__init__()
        self.image = pygame.image.load('graphics/wall.png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed
    def wall_move(self,direction):
        if direction == 'Left':
            self.rect.x -=self.speed
        elif direction == 'Right':
            self.rect.x+=self.speed