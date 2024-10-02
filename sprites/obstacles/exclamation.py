import pygame

class Exclamation(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,size,pos):
        super().__init__()
        self.image = pygame.image.load("graphics/Exclamation-Point.png")
        self.image = pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.realX = pos[0]
        self.realY = pos[1]
    def spawnExclamation(self,rPos,counter):
 # Only call this once
        if counter == 0:
            self.rect.x = rPos[0]
            self.rect.y = rPos[1] + 2250
            self.realX = rPos[0]    
            self.realY = rPos[1]        
        if counter % 20 >= 0 and counter % 20 <=5:
            self.rect.x = self.realX
            self.rect.y = self.realY + 2250
        else:
            self.rect.x = 9000

