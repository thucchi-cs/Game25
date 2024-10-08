import pygame

class Rocks(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,size,rPos,speed):
        super().__init__()
        # Load image
        self.image = pygame.image.load("graphics/rock.png")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = rPos[0]
        self.rect.y = rPos[1]

        # Movements variables
        self.lineX = rPos[0]
        self.lineY = rPos[1] + 2000
        self.actualRY = rPos[1]
        self.actualLY = self.actualRY + 2000
        self.speed = speed
        self.counter = 0
        self.exclamation = self.Exclamation((100,100),(9000,0))
    
    # Update - periodic
    def update(self):
        self.check_line()

    # Check if fly has reached the invisible line
    def check_line(self):
        if self.actualLY >=0:
            if self.rect.y < 0:
                self.exclamation.spawnExclamation((self.rect.x,self.actualRY),self.counter)
            else:
                self.exclamation.rect.x = 9000
            self.fall_rock()
        # It is going up, so Y. higher Y


    # Width is 500. 500 / 5 = 100 length rocks... ?
    # Animate rock falling down
    def fall_rock(self):
        self.counter +=1
        if self.counter % 2 == 1:
            self.actualRY += self.speed
            self.rect.y = self.actualRY

    # Scroll with screen
    def scroll(self,direction,moveSpeed):
        # if direction == 'D':
        #     self.rect.y +=moveSpeed # Speed is always 2, so -2 y per thing
        #     self.actualLY += moveSpeed
        #     self.actualRY += moveSpeed

        # elif direction == 'U':
        #     self.rect.y += moveSpeed
        #     self.actualRY += moveSpeed
        #     self.actualLY += moveSpeed
        pass

    # Remove from sprite groups
    def remove(self):
        if self.rect.y > 600:
            self.groups[0].remove(self)

    # Warning exclamation mark
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

        # Show on screen
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

