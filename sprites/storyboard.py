import pygame
import constants
import sprites.music as m

class StoryBoard(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        super().__init__()
        # Load image and rect
        self.image = pygame.image.load("graphics/storyboard.png")
        self.rect = self.image.get_rect()
        pygame.mixer.init()
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
        self.counter = 0
        self.curr_pt = 0
        self.rect.topleft = self.stop_points[self.curr_pt]
        self.speed = 30

        self.soundlist = [pygame.mixer.Sound("music/frame1.ogg"),
                          pygame.mixer.Sound("music/frame2.ogg"),
                          pygame.mixer.Sound("music/frame3.ogg"),
                          pygame.mixer.Sound("music/frame4.ogg"),
                          pygame.mixer.Sound("music/frame5.ogg"),
                          pygame.mixer.Sound("music/frame6.ogg"),
                          pygame.mixer.Sound("music/frame7.ogg"),
                          pygame.mixer.Sound("music/frame8.ogg"),
                          pygame.mixer.Sound("music/frame9.ogg"),
                          ]
        pygame.mixer.Sound.play(self.soundlist[0])
    def draw(self):
        constants.SCREEN.blit(self.image, (self.rect.x, self.rect.y))
    
    def next_point(self):
        self.curr_pt += 1
        self.curr_pt %= len(self.stop_points)
        self.rect.topleft = self.stop_points[self.curr_pt]
         
    def glide(self, next_point):                
        last_pt = self.stop_points[next_point - 1]
        next_pt = self.stop_points[next_point]
    
        if last_pt[0] != next_pt[0]:
            distX = abs(next_pt[0] - last_pt[0])
            middleX = distX // 2
            distX_from_mid = (abs(middleX - abs(self.rect.x - last_pt[0]))) % middleX
            speedX_proportion = 1- (distX_from_mid / middleX)
            speedX = round(self.speed * speedX_proportion)
            speedX = 1 if speedX == 0 else speedX
            speedX *= -1 if last_pt[0] > next_pt[0] else 1
            self.rect.x += speedX
        
        if last_pt[1] != next_pt[1]:
            distX = abs(next_pt[1] - last_pt[1])
            middleX = distX // 2
            distX_from_mid = (abs(middleX - abs(self.rect.y - last_pt[1]))) % middleX
            speedX_proportion = 1- (distX_from_mid / middleX)
            speedX = round(self.speed * speedX_proportion)
            speedX = 1 if speedX == 0 else speedX
            speedX *= -1 if last_pt[1] > next_pt[1] else 1
            self.rect.y += speedX

        rangeX = [next_pt[0] - 2, next_pt[0] + 2]
        rangeY = [next_pt[1] - 2, next_pt[1] + 2]
                
        if (min(rangeX) <= self.rect.x <= max(rangeX)) and (min(rangeY) <= self.rect.y <= max(rangeY)):
            self.rect.topleft = next_pt
            self.curr_pt += 1
            pygame.mixer.Sound.stop(self.soundlist[self.counter])
            self.counter +=1
            pygame.mixer.Sound.play(self.soundlist[self.counter])


            return True
        
        return False