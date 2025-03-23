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
import levels.restart as restart
import levels.instructions as instructions
import levels.story as story
import levels.player_selection as play_select
import levels.end as end
import levels.tutorial as tutorial

# Music
pygame.mixer.init()
pygame.mixer.music.load('music/cave-9207.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
# Game
async def main():
    while True:

        # show reference grid - comment / uncomment to show / hide reference grid 
        # quit = await grid.screen()
        # if quit:
        #     return
            
        
        # Run main menu
        status = await title.menu()
        if status == "quit":
            return     
        
        status = await story.storyboard()
        if status == "quit":
            return
        
        status = await play_select.menu()
        if status == "quit":
            return 
        player_count = len(players)

        # Run Instructions Screen
        # status = await instructions.showInstructions()
        # if status == "quit":
        #     return 
        
        status = "restart"
        while status == "restart":
            status = await tutorial.level()
            if status == "quit":
                return
            h.reset_sprites()
            if status == "menu":
                break
            if status == "dead":
                await restart.restart()
                status = "restart"
        if status == "menu":
            continue
        
        # Run level1
        for lvl in range(1, 4):
            status = "restart"
            while status == "restart":
                status = await level.level(lvl)
                if status == "quit":
                    return
                h.reset_sprites()
                if status == "menu":
                    break
                if status == "dead":
                    await restart.restart()
                    status = "restart"
            print(status)
            if status == "menu":
                break
            # Run level one transitionw
            status = await transition.transition(lvl+1, player_count)
            if status == "quit":
                return
            
        if status == "menu":
            continue
        
        status = await end.End()
        if status == "quit":
            return



asyncio.run(main())