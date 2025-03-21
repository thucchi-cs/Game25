import pygame
import constants

class StoryBoard(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        super().__init__()
        # Load image and rect
        self.image = pygame.image.load("graphics/storyboard.png")
        self.rect = self.image.get_rect()
        self.stop_points = [
            (-90, -40),
            (-637, -40),
            (-1187, -40),
            (-1187, -598),
            (-637, -598),
            (-90, -598),
            (-90, -1155),
            (-637, -1155),
            (-1187, -1155) 
        ]
        self.curr_pt = 0
        self.rect.topleft = self.stop_points[self.curr_pt]
        self.speed = 50
        
    def draw(self):
        constants.SCREEN.blit(self.image, (self.rect.x, self.rect.y))
    
    def next_point(self):
        self.curr_pt += 1
        self.curr_pt %= len(self.stop_points)
        self.rect.topleft = self.stop_points[self.curr_pt]
        
    def glide(self, next_point):        
        print("current", self.rect.topleft)
        
        last_pt = self.stop_points[next_point - 1]
        next_pt = self.stop_points[next_point]
        
        print("lastpt", last_pt)
        print("nextpt", next_pt)
        
        if last_pt[0] != next_pt[0]:
            distX = abs(next_pt[0] - last_pt[0])
            print("distX", distX)
            middleX = distX // 2
            print("midX", middleX) 
            distX_from_mid = (abs(middleX - abs(self.rect.x - last_pt[0]))) % middleX
            print("distX_fromMid", distX_from_mid)
            speedX_proportion = 1- (distX_from_mid / middleX)
            print("speedXprop", speedX_proportion)
            speedX = round(self.speed * speedX_proportion)
            print("speedX", speedX)
            speedX = 1 if speedX == 0 else speedX
            speedX *= -1 if last_pt[0] > next_pt[0] else 1
            print("speedX", speedX)
            self.rect.x += speedX
            print("rectX", self.rect.x)
        
        if last_pt[1] != next_pt[1]:
            distX = abs(next_pt[1] - last_pt[1])
            print("distY", distX)
            middleX = distX // 2
            print("midY", middleX) 
            distX_from_mid = (abs(middleX - abs(self.rect.y - last_pt[1]))) % middleX
            print("distY_fromMid", distX_from_mid)
            speedX_proportion = 1- (distX_from_mid / middleX)
            print("speedYprop", speedX_proportion)
            speedX = round(self.speed * speedX_proportion)
            print("speedY", speedX)
            speedX = 1 if speedX == 0 else speedX
            speedX *= -1 if last_pt[1] > next_pt[1] else 1
            print("speedY", speedX)
            self.rect.y += speedX
            print("rectY", self.rect.y)

        rangeX = [next_pt[0] - 2, next_pt[0] + 2]
        rangeY = [next_pt[1] - 2, next_pt[1] + 2]
        
        print("rangeX", rangeX)
        print("rangeY", rangeY)
                
        if (min(rangeX) <= self.rect.x <= max(rangeX)) and (min(rangeY) <= self.rect.y <= max(rangeY)):
            self.rect.topleft = next_pt
            self.curr_pt += 1
            print("done")
            return True
        print()
        return False