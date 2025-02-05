# Libraries import
import asyncio
import pygame

# Files imports
import levels.level3 as level3
import levels.title as title
import levels.grid as grid
from constants import *
import levels.transition as transition

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
    
    player_count = len(players)

    # Run level1
    quit = await level3.level(1)
    if quit:
        return

    # Run level one transitionw
    quit = await transition.transition(2, player_count)
    if quit:
        return
    
    # Run level3
    quit = await level3.level(2)
    if quit:
        return
    
    quit = await transition.transition(3, player_count)
    if quit:
        return
    
    # Run level3
    quit = await level3.level(3)
    if quit:
        return



asyncio.run(main())