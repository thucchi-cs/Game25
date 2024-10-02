import pygame

class Wall(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos,Kspeed):
        super().__init__()
        self.image = pygame.image.load('graphics/wall.png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = Kspeed
        self.actualX = pos[0]
        self.actualY = pos[1]

    # Move off screen
    def wall_move(self, direction,speed):
        if direction == 'D':
            self.rect.y +=speed 
            self.actualY += speed
        elif direction == 'U':
            self.rect.y+=speed
            self.actualY += speed
