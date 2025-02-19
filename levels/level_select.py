import asyncio
import pygame
import sprites.menuButtons as btn
import globals
from globals import *

async def select_level():
    # Query the database for the number of levels unlocked
    # response = supabase.table("player_progress").select("levels_unlocked").eq("player_name", "Test2").execute()
    # Total number of levels unlocked converted to a single integer
    # levels_unlocked = response.data[0]["levels_unlocked"]
    # Level selection buttons
    level1_btn = btn.menuBtn((50, 50), (250, 450), 'player2button.png')
    level2_btn = btn.menuBtn((50, 50), (250, 350), 'player3button.png')
    level3_btn = btn.menuBtn((50, 50), (250, 400), 'player4button.png')
    btns_lst = [level1_btn, level2_btn, level3_btn]
    btns = pygame.sprite.Group()

    # For every level, if the level is unlocked, add it to the button group
    for lvl in range(1, num_of_levels+1):
        if lvl <= globals.player_data.get("levels_unlocked"):
            btns.add(btns_lst[lvl-1])
    
    run = True
    while run:
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                return "quit"
            # Check if button is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Return selected level
                for i in range(len(btns.sprites())):
                    if btns.sprites()[i].is_clicked():
                        return i+1
        
        SCREEN.fill((0,200,0))
        btns.draw(SCREEN)

        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)


