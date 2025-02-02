# Libraries import
import asyncio
import pygame

# Files imports
import levels.level1 as level1
import levels.level3 as level3
import levels.title as title
import levels.grid as grid
from constants import *
import levels.helpers as helpers

# Music
pygame.mixer.init()
pygame.mixer.music.load('music/life.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
# Game
async def main():

    # show reference grid - comment / uncomment to show / hide reference grid 
    # quit = await grid.screen()
    # if quit:
    #     return

    # Run main menu
    quit = await title.menu()
    if quit:
        return
    
    # Run level one transition
    quit = await helpers.transition(1)
    if quit:
        return
    
    # Run level1
    quit = await level1.level()
    if quit:
        return

    # Run level one transition
    quit = await helpers.transition(2)
    if quit:
        return
    
    # Run level3
    quit = await level3.level()
    if quit:
        return



asyncio.run(main())