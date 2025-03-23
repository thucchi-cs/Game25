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
import levels.story as story
import levels.player_selection as play_select
import levels.end as end
import sprites.music as m
import levels.tutorial as tutorial
import math

# Music
pygame.mixer.init()
menu_music = m.Music("title_screen")
cutscene_music = m.Music("cutscene")
game_music = m.Music("game_audio")

win_music = pygame.mixer.Sound("music/final_win.ogg")
winSound = pygame.mixer.Sound("music/level_win.ogg")

# Game
async def main():
    while True:

        # show reference grid - comment / uncomment to show / hide reference grid 
        # quit = await grid.screen()
        # if quit:
        #     return
            
        # Main menu music
        menu_music.load()
        for i in range(100):
            menu_music.fade_in()
            
        # Run main menu
        status = await title.menu()
        if status == "quit":
            return
        for i in range(100):     
            menu_music.fade_out()

        # storyboard music
        cutscene_music.load()
        for i in range(100):
            cutscene_music.fade_in()

        # Run cutscene
        status = await story.storyboard()
        if status == "quit":
            return
        
        # Player selection
        status = await play_select.menu()
        if status == "quit":
            return 
        player_count = len(players)
        
        # Tutorial level
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
        
        # Load music
        game_music.load()
        for i in range(100):
            game_music.fade_in()
        
        # Run levels 1-3
        for lvl in range(1, 4):
            level_time = 0
            status = "restart"
            tries = 1
            while status == "restart":
                status, level_time = await level.level(lvl)
                if status == "quit":
                    return
                h.reset_sprites()
                if status == "menu":
                    break
                elif status == "dead":
                    await restart.restart()
                    status = "restart"
                if status == "restart":
                    tries += 1
            if status == "menu":
                break
            # Run level transitionw
            pygame.mixer.Sound.set_volume(winSound,0.3)
            pygame.mixer.Sound.play(winSound)
            status = await transition.transition(lvl+1, player_count, tries, level_time)
            if status == "quit":
                return
            
        if status == "menu":
            continue
        
        # Load music
        pygame.mixer.music.fadeout(1)
        pygame.mixer.Sound.set_volume(win_music,0.1)
        pygame.mixer.Sound.play(win_music)
        
        # Ending screen
        status = await end.End()
        if status == "quit":
            return



asyncio.run(main())