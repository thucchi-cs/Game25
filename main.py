# Libraries import
import asyncio
import pygame

# Files imports
import levels.level1 as level1
from constants import *

# Music
pygame.mixer.init()
pygame.mixer.music.load('music/life.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
# Game
async def main():
    # Run level 1
    quit = await level1.level()
    if quit:
        return
    



asyncio.run(main())