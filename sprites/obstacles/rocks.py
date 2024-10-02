import pygame

class Rocks(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,size,rPos,speed,moveSpeed):
        super().__init__()
        self.image = pygame.image.load("graphics/rock.png")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = rPos[0]
        self.rect.y = rPos[1]
        self.speed = speed
        self.lineX = rPos[0]
        self.lineY = rPos[1] + 2000
        self.actualRY = rPos[1]
        self.actualLY = self.actualRY + 2000
        self.change = 0
        self.counter = 0
        self.moveSpeed = int(moveSpeed)
    
    def check_line(self,playerY,exclamations):
        if self.actualLY >=0:
            if self.rect.y < 0:
                for exclamation in exclamations:
                    exclamation.spawnExclamation((self.rect.x,self.actualRY),self.counter)
            else:
                for exclamation in exclamations:
                    exclamation.rect.x = 9000
            self.fall_rock()
        else:
            pass
        # It is going up, so Y. higher Y


        # Width is 500. 500 / 5 = 100 length rocks... ?
    def fall_rock(self):
        self.counter +=1
        if self.counter % 2 == 1:
            self.actualRY += self.speed
            self.rect.y = self.actualRY
        else:
            pass

    def rock_move(self,direction,moveSpeed):

        if direction == 'D':
            self.rect.y +=moveSpeed # Speed is always 2, so -2 y per thing
            self.actualLY += moveSpeed
            self.actualRY += moveSpeed
            self.change += moveSpeed

        elif direction == 'U':
            self.rect.y += moveSpeed
            self.actualRY += moveSpeed
            self.actualLY += moveSpeed
            self.change +=moveSpeed


    def remove(self,rocks):
        if self.rect.y > 600:
            self.groups[0].remove(self)
            

