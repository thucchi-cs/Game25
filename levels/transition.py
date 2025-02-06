import asyncio
from constants import *
import sprites.text as text
import sprites.flies as flies
import pygame
import levels.helpers as h


async def transition(level_num, player_count):
    # Fly list used to reset player list 

    # Get rid of the previous level's obstacles
    h.reset_sprites()

    # Variables for fly display
    display_flies_list = [flies.Flies(225, 1025, ARROWS, 1), flies.Flies(275, 1050, WASD, 2), flies.Flies(175, 1000, TFGH, 3), flies.Flies(325, 1075, IJKL, 4)]
    display_flies_list = [display_flies_list[i] for i in range(player_count)]
    if player_count == 3:
        for fly in display_flies:
            fly.rect.centerx += 25
    display_flies = pygame.sprite.Group(display_flies_list)
    moving = True
    clicked = False
    total_moved = 0

    # Background variables
    background = pygame.image.load("graphics/dirt_wipe.png")
    background_pos = [0, -600]


    # Text variables
    nice_job_text = text.Text("fonts/COMIC.ttf", 30, f"Level {level_num-1} Complete!", (255,255,255), 250, 200)
    continue_text = text.Text("fonts/COMIC.ttf", 20, f"Click Anywhere to Continue to Next Level", (255,255,255), 250, 300)
    
    # Loop variables
    clock = pygame.time.Clock()
    quit = False
    run = True
    while run:
        # Event handles
        # clock.tick(FPS)
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        if total_moved > 120:
            run = False
    
        moving = False if total_moved == 60 else True
        if moving or clicked:
            total_moved += 1
            background_pos[1] += 5
            for fly in display_flies:
                fly.rect.centery -= 10

        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background, background_pos)
        nice_job_text.blit_text(SCREEN)
        continue_text.blit_text(SCREEN)
        display_flies.update()
        display_flies.draw(SCREEN)

        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    
    return "quit" if quit else "continue"