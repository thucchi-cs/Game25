import pygame

class Water(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load("graphics/water.png")
        self.image = pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect()
        self.size = size
        self.pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.realX = pos[0]
        self.realY = pos[1]
        self.counter = 0
        self.counter2 = 0
        self.counter3 = 1
    def animate(self,pressed):
        self.counter +=1
        if not pressed:
            if self.counter == 1 or self.counter == 2:
                self.image = pygame.image.load("graphics/water-2.png")
                self.image = pygame.transform.scale(self.image,self.size)
                self.rect = self.image.get_rect()
                self.rect.x = self.realX
                self.rect.y = self.realY
            elif self.counter == 3 or self.counter == 4:
                self.image = pygame.image.load("graphics/water-3.png")
                self.image = pygame.transform.scale(self.image,self.size)
                self.rect = self.image.get_rect()
                self.rect.x = self.realX
                self.rect.y = self.realY
            elif self.counter == 5 or self.counter == 6:
                self.image = pygame.image.load("graphics/water-4.png")
                self.image = pygame.transform.scale(self.image,self.size)
                self.rect = self.image.get_rect()
                self.rect.x = self.realX
                self.rect.y = self.realY
            elif self.counter == 7 or self.counter == 8:
                self.image = pygame.image.load("graphics/water-5.png")
                self.image = pygame.transform.scale(self.image,self.size)
                self.rect = self.image.get_rect()
                self.rect.x = self.realX
                self.rect.y = self.realY
            elif self.counter == 9 or self.counter == 10:
                self.image = pygame.image.load("graphics/water.png")
                self.image = pygame.transform.scale(self.image,self.size)
                self.rect = self.image.get_rect()
                self.rect.x = self.realX
                self.rect.y = self.realY
            else:
                self.counter = 0
        
    def water_move(self, direction,speed):
        if direction == 'D':
            self.rect.y +=speed 
            self.realY += speed
        elif direction == 'U':
            self.rect.y+=speed
            self.realY += speed
    def water_button_pressed(self,pressed):
        if pressed and self.counter2 <= 24:
            self.counter2 +=1
            if self.counter2 %5 == 0:
                self.counter3 +=1
            if self.counter2 % 5 >= 0 and self.counter2 % 5 <=2:
                self.image = pygame.image.load("graphics/water-"+str(self.counter3)+"-open.png")
                self.image = pygame.transform.scale(self.image,self.size)
                self.rect = self.image.get_rect()
                self.rect.x = self.realX
                self.rect.y = self.realY
            else:
                self.rect.x = self.pos[0]
                self.realX = self.pos[0]
        elif pressed:
            self.rect.x = 9000
            self.realX = 9000
        # else:
        #     self.rect.x = self.pos[0]
        #     self.realX = self.pos[0]
        

    def remove(self):
        pass