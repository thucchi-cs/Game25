import pygame
import globals

class Web(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos, rot=0, type="circle"):
        super().__init__()
        # Load image and position
        self.size = size
        self.image_path = f'graphics/webs/{type}_web.png'
        self.image = pygame.image.load(self.image_path)
        self.height = size/2 if type == "wall" else size
        self.image = pygame.transform.smoothscale(self.image, (size,self.height))
        # Rotation based off direction
        self.image = pygame.transform.rotate(self.image, rot)
        self.rect = self.image.get_rect(center=pos)

    # Scroll with screen
    def scroll(self, addition):
        self.rect.y += globals.SPEED + addition