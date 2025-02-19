import pygame
import globals
import sprites.text as text
import sprites.shell as shell

class Key(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphics/key.png")
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.counter = 0
        self.pos = 0
        self.following = False
        self.path = []
        self.collected = False
        self.gate = None
    
    def scroll(self, addition):
        self.rect.y += globals.SPEED + addition
        # self.bounce()
    
    def bounce(self):
        self.counter += 1
        self.rect.y += self.speed
        if self.counter % 7 == 0:
            self.speed *= -1
    
    def update(self):
        if self.following:
            self.animate()
    
    def set_path(self, path):
        self.path = path
        
    def set_gate(self, gate):
        self.gate = gate
        
    def animate(self):
        if self.pos < len(self.path):
            self.rect.centerx = self.path[self.pos][0]
            self.rect.centery = self.path[self.pos][1]
            self.pos += 1
        else:
            self.following = False
            if not self.collected:
                globals.key_counter.counter += 1
                self.remove(globals.all)
                self.add(globals.keys_collected)
                self.pos = 0
                self.collected = True
            else:
                self.remove(globals.all, globals.keys_collected)
                self.gate.clearing = True
                self.kill()
                
class KeyCounter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/key.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = 431
        self.rect.y = 10
        self.counter = 0
        self.text = text.Text("fonts/COMIC.TTF", 20, str(self.counter), (255,255,255), 479, 23)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.text.text = str(self.counter)
        self.text.blit_text(screen)