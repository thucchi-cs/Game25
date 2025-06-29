# Libraries import
import asyncio
import pygame

# Files imports
import levels.level as level
import levels.title as title
import levels.animation as animation
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
import levels.level_selection as level_select

# Music
pygame.mixer.init()
menu_music = m.Music("title_screen")
cutscene_music = m.Music("cutscene")
game_music = m.Music("game_audio")

level_win = m.Music("level_win")
game_win = m.Music("final_win")

win_music = pygame.mixer.Sound("music/final_win.ogg")
winSound = pygame.mixer.Sound("music/level_win.ogg")

# Game
async def main():

    # Intro animation
    # menu_music.load()
    # status = await animation.animation()
    # if status == "quit":
    #     return

    while True:
        reset_status()
        # show reference grid - comment / uncomment to show / hide reference grid 
        # quit = await grid.screen()
        # if quit:
        #     return
        
        # players.empty()
        # players.add(fly1,fly2,fly3,fly4)
        # all.add(fly1,fly2,fly3,fly4)
            
        # # Main menu music
        # if not menu_music.playing:
        #     menu_music.load()

        # # Run main menu
        # status = await title.menu()
        # if status == "quit":
        #     return
        # # for i in range(100):     
        # #     menu_music.fade_out()
        # menu_music.unload()

        # # storyboard music
        # cutscene_music.load()
        # pygame.mixer.music.set_volume(0.1)

        # # Run cutscene
        # status = await story.storyboard()
        # if status == "quit":
        #     return
        
        # Player selection
        status = await play_select.menu()
        if status == "quit":
            return 
        player_count = len(players)
        
        h.reset_sprites()

        lvl = 0
        while not level_status["win"]:
            status = await level_select.menu()
            if status == "quit":
                return 
            
            if status[1] == 0:
                # Tutorial level
                status = "restart"
                # Play tutorial until win or skip
                while status == "restart":
                    status = await tutorial.level()
                    # End game
                    if status == "quit":
                        return
                    h.reset_sprites()
                    # Back out to main menu
                    if status == "menu":
                        break
                    # Die and restart
                    if status == "dead":
                        await restart.restart()
                        status = "restart"
                
                # Load music
                cutscene_music.unload()
                pygame.mixer.music.set_volume(0.2)
            
            else:
                game_music.load()
                level_time = 0
                lvl = status[1]
                status = "restart"
                tries = 1
                
                # Play level until win or quit
                while status == "restart":
                    status, level_time = await level.level(lvl)
                    # End game
                    if status == "quit":
                        return
                    h.reset_sprites()
                    # Back out to main menu
                    if status == "menu":
                        break
                    # Die and restart
                    elif status == "dead":
                        await restart.restart()
                        status = "restart"
                    # Restart
                    if status == "restart":
                        tries += 1
                # Return to main menu
                if status == "menu":
                    break

                # Run level transitionw
                game_music.unload()
                level_win.load(0)

                status = await transition.transition(lvl+1, player_count, tries, level_time)
                if status == "quit":
                    return
            
            level_status["win"] = True
            for i in range(1,4):
                level_status["win"] = level_status["win"] and (level_status[f"lvl{i}"] == "Played")
                if not level_status["win"]:
                    break

        # Restart to main menu
        if status == "menu":
            continue
        
        # Load music
        game_music.unload()
        pygame.mixer.Sound.set_volume(win_music,0.1)
        pygame.mixer.Sound.play(win_music)
        
        # Ending screen
        status = await end.End()
        if status == "quit":
            return

# Run the game
asyncio.run(main())