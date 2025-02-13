# Libraries import
import asyncio
import pygame

# Files imports
import levels.level as level
import levels.title as title
import levels.grid as grid
from constants import *
import levels.transition as transition
import levels.helpers as h
import levels.instructions as instructions
import levels.player_selection as player_selection
import levels.level_select as level_select

# Music
pygame.mixer.init()
pygame.mixer.music.load('music/life.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
# Game
async def main():

    # show reference grid - comment / uncomment to show / hide reference grid 
    # quit = await grid.screen()dnf
    # if quit:
    #     return

    # Run main menu
    status = await title.menu()
    if status == "quit":
        return 
    player_count = len(players)
    
    # Run Instructions Screen
    status = await instructions.showInstructions()
    if status == "quit":
        return 

    while True:    
        lvl = await level_select.select_level()
        if lvl == "quit":
            return

        status = "restart"
        while status == "restart":
            status = await level.level(lvl)
            if status == "quit":
                return
            h.reset_sprites()
            # if status == 

        # Run level transition
        status = await transition.transition(lvl+1, player_count)
        if status == "quit":
            return

    # Run level
    # for lvl in range(1, 4):
    #     status = "restart"
    #     while status == "restart":
    #         status = await level.level(lvl)
    #         if status == "quit":
    #             return
    #         h.reset_sprites()
    #         # if status == 

    #     # Run level transition
    #     status = await transition.transition(lvl+1, player_count)
    #     if status == "quit":
    #         return



asyncio.run(main())