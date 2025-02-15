import pygame
import constants

class Water(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,pos,size):
        super().__init__()
        # Load image
        self.images = [pygame.transform.scale(pygame.image.load(f"graphics/newGraphics/WaterRed{i}.png"), size) for i in range(1, 4)]
        self.image = self.images[0]
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

            self.counter %= 10
            findex = self.counter //5 # This changes to a new image every 2 frames
            # print(findex)
            self.image = self.images[findex]
            self.rect.x = self.realX if self.show else 9000
        
    # Scroll with screen
    def scroll(self, addition):
        self.rect.y += constants.SPEED + addition
        
    # Animate opening and closing
    def animation(self):
        if self.counter2 <= 24:
            self.counter2 += 1
            if self.counter2 %5 == 0:
                self.counter3 += 1 if self.clearing else -1
            if self.counter2 % 5 >= 0 and self.counter2 % 5 <=2:
                self.image = pygame.image.load("graphics/newGraphics/WaterRedPath"+str(self.counter3)+".png")
                self.image = pygame.transform.scale(self.image,self.size)
            else:
                self.rect.x = self.pos[0]
                self.realX = self.pos[0]
        else:
            self.show = self.appearing
            self.counter2 = 0
            self.clearing = False
            self.appearing = False