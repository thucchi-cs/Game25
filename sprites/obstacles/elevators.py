import pygame
import constants
import sprites.shell as shell

class Elevators(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pos, size, flipped, y2):
        super().__init__()
        # Load image
        self.image = pygame.image.load("graphics/newGraphics/Elevatorred.png")
        self.image = pygame.image.load("graphics/elevator.png")
        self.image = pygame.transform.scale(self.image, size)
        self.image = pygame.transform.flip(self.image, flip_x= flipped, flip_y= False)
        self.flipped = flipped
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.y = pos[0], pos[1]
        
        # Moving varibles
        self.dest = y2
        self.start = pos[1]
        dist = abs(self.start - self.dest)
        self.speed = dist // 50
        self.speed *= 1 if self.dest > self.rect.y else -1
        self.clearing = False
        self.appearing = False

        self.inner = shell.Collide_Box(self.rect, 2)
        self.update_inner_box()

    # Move to destination
    def animation(self):
        if ((abs(self.rect.y - self.dest) > 3) and self.clearing) or ((abs(self.rect.y - self.start) > 3) and self.appearing):
            # Move
            self.rect.y += self.speed if self.clearing else -self.speed
            
            # Avoid crushing a fly
            for fly in constants.players:
                if pygame.sprite.collide_mask(self, fly) and not fly.elevator_collide(self):
                    self.rect.y -= self.speed if self.clearing else -self.speed
                    
        else:
            self.clearing = False
            self.appearing = False

    # Update - periodic
    def update(self):
        if self.clearing or self.appearing:
            self.animation()

        self.update_inner_box()

    # Scroll with screen
    def scroll(self, addition):
        self.rect.y += constants.SPEED + addition
        self.dest += constants.SPEED + addition
        self.start += constants.SPEED + addition

    def update_inner_box(self):
        back_w = (10/86) * self.rect.width
        top_w = (13/109) * self.rect.height
        h = ((109-12-13)/109) * self.rect.height
        x = self.rect.x if not self.flipped else self.rect.x + back_w
        y = self.rect.y + top_w
        w = self.rect.width - back_w
        self.inner.new_box(x,y,w,h)
