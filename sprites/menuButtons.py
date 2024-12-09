import pygame

# Button for menu
class menuBtn(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, size, pos, img):
        super().__init__()
        # Load image and rect
        self.image = pygame.image.load(f'graphics/menu_buttons/{img}')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    # Check if is being clicked by mouse
    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
