import pygame
import constants
# Pause
class Music(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,music):
        super().__init__()
        # Load image and rect
        self.music = music
        self.volume = 0.2
        self.playing = False
    def load(self,looping=-1):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load("music/" + self.music + ".ogg")
        pygame.mixer.music.play(looping)
        self.playing = True
    def unload(self):
        pygame.mixer.init()
        pygame.mixer.music.stop()
        self.playing = False
    def queue(self):
        pygame.mixer.init()
        pygame.mixer.music.queue("music/" + self.music + ".ogg")

    
        

    def fade_in(self):
        print("yay", self.volume)
        if self.volume >= 0.2:
            pygame.mixer.music.set_volume(self.volume)
            return
        self.volume += 0.01
        pygame.mixer.music.set_volume(self.volume)


    def fade_out(self):
        if self.volume <= 0:
            return
        self.volume -= 0.01
        print("aw", self.volume)
        pygame.mixer.music.set_volume(self.volume)
