import pygame

class Wall(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos,speed):
        super().__init__()
        self.image = pygame.image.load('graphics/wall.png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed

    # Move off screen
    def wall_move(self, direction):
        if direction == 'D':
            self.rect.y -=self.speed
        elif direction == 'U':
            self.rect.y+=self.speed