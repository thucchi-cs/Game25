import pygame
import constants

class Buttons(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, pos, rot, temp, obstacle):
        super().__init__()
        # Load image
        self.size = (50, 25)
        self.rot = rot
        self.temp = temp
        self.images = [
            'graphics/ButtonRedUp.png' if not temp else 'graphics/ButtonGreenUp.png',
            'graphics/ButtonRedDown.png' if not temp else 'graphics/ButtonGreenDown.png'
        ]
        self.counter = 0
        self.image_index = 0
        self.image_path = self.images[0]
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)
        self.image = pygame.transform.rotate(self.image, self.rot)
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.collide = self.Collide_Box(self.rect)
        self.pressed = False
        self.obstacle = obstacle  
        

    # When pressed
    def press(self):
        # Change image
        x, y = self.rect.centerx, self.rect.centery
        self.image_index = 1 - self.image_index
        self.image_path = self.images[self.image_index]
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)
        self.image = pygame.transform.rotate(self.image, self.rot)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
        self.pressed = not self.pressed

        # Remove/add obstacle
        self.obstacle.clearing = self.pressed
        self.obstacle.appearing = not self.pressed

        # Return state of button
        return self.pressed

    # Scroll with screen
    def scroll(self, addition):
        self.rect.y += constants.SPEED + addition

    def update(self):
        self.collide.update(self.rect)
        collide_fly = False
        for fly in constants.players:
            if self.collide.rect.colliderect(fly):
                collide_fly = True
                break
        if self.temp and self.pressed and not collide_fly:
            self.counter += 1
            if self.counter >= 100:
                self.press()
                self.counter = 0
        # pygame.draw.rect(constants.SCREEN, (255,255,255),(self.collide.rect),1)

    class Collide_Box(pygame.sprite.Sprite):
        def __init__(self, rect):
            super().__init__()
            self.shell = 3
            self.rect = pygame.Rect(rect.x - self.shell, rect.y - self.shell, rect.width + 2*self.shell, rect.height + 2*self.shell)
        def update(self, rect):
            self.rect = pygame.Rect(rect.x - self.shell, rect.y - self.shell, rect.width + 2*self.shell, rect.height + 2*self.shell)
