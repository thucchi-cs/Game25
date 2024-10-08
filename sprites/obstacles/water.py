import pygame

class Water(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,pos,size):
        super().__init__()
        # Load image
        self.image = pygame.image.load("graphics/water.png")
        self.image = pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect()
        self.size = size
        self.pos = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.realX = pos[0]
        self.realY = pos[1]

        # Timing variables
        self.counter = 0
        self.counter2 = 0
        self.counter3 = 1

        # Animation variables
        self.clearing = False
        self.appearing = False
        self.appear = False
        self.show = True

    # Update - periodic
    def update(self):
        # Animate appearing and disappearing if needed
        if self.clearing or self.appearing:
            self.animation()

        else:
            # Water flowing animation
            self.counter +=1
            if self.counter == 1 or self.counter == 2:
                self.image = pygame.image.load("graphics/water-2.png")
            elif self.counter == 3 or self.counter == 4:
                self.image = pygame.image.load("graphics/water-3.png")
            elif self.counter == 5 or self.counter == 6:
                self.image = pygame.image.load("graphics/water-4.png")
            elif self.counter == 7 or self.counter == 8:
                self.image = pygame.image.load("graphics/water-5.png")
            elif self.counter == 9 or self.counter == 10:
                self.image = pygame.image.load("graphics/water.png")
            else:
                self.counter = 0
            self.image = pygame.transform.scale(self.image,self.size)
            self.rect.x = self.realX if self.show else 9000
        
    # Scroll with screen
    def scroll(self, direction,speed):
        # if direction == 'D':
        #     self.rect.y +=speed 
        #     self.realY += speed
        # elif direction == 'U':
        #     self.rect.y+=speed
        #     self.realY += speed
        pass
    # Animate opening and closing
    def animation(self):
        if self.counter2 <= 24:
            self.counter2 += 1
            if self.counter2 %5 == 0:
                self.counter3 += 1 if self.clearing else -1
            if self.counter2 % 5 >= 0 and self.counter2 % 5 <=2:
                self.image = pygame.image.load("graphics/water-"+str(self.counter3)+"-open.png")
                self.image = pygame.transform.scale(self.image,self.size)
            else:
                self.rect.x = self.pos[0]
                self.realX = self.pos[0]
        else:
            self.show = self.appearing
            self.counter2 = 0
            self.clearing = False
            self.appearing = False