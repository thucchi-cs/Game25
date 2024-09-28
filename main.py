# Libraries import
import asyncio
import pygame

# Files imports
import levels.level1 as level1
from constants import *

# Music
pygame.mixer.init()
pygame.mixer.music.load('music/GARREG.mp3')
pygame.mixer.music.play(-1)

# Game
async def main():
    # Run level 1
    quit = await level1.level()
    if quit:
        return
    

asyncio.run(main())