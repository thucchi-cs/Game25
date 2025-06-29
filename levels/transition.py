import asyncio
from constants import *
import sprites.text as text
import sprites.flies as flies
import pygame
import levels.helpers as h
import levels.end as end
import sprites.images as img


async def transition(level_num, player_count, level_tries, level_time):
    
    clock = pygame.time.Clock()
    # if level_num == 4:
    #     await h.fade_out_animation(clock)
    #     status = await end.End()
    #     return status
    
    # Get rid of the previous level's obstacles
    h.reset_sprites()

    # Variables for fly display
    display_flies_list = [flies.Flies(225, 1025, ARROWS, 1), flies.Flies(275, 1050, WASD, 2), flies.Flies(175, 1000, TFGH, 3), flies.Flies(325, 1075, IJKL, 4)]
    display_flies_list = [display_flies_list[i] for i in range(player_count)]
    display_flies = pygame.sprite.Group(display_flies_list)
    if player_count == 3:
        for fly in display_flies:
            fly.rect.centerx += 25
    moving = True
    clicked = False
    total_moved = 0

    # Background variables
    background = pygame.image.load("graphics/dirt_wipe.png")
    background_pos = [0, -600]

    # Time Varibales
    minutes = level_time // 60
    minutes = str(minutes) + " Minutes and" if minutes > 1 else str(minutes) + " Minute and" if minutes > 0 else ""
    seconds = level_time % 60
    seconds = str(seconds) + " Seconds" if seconds > 1 else str(seconds) + " Second" if seconds > 0 else ""

    # Text variables
    nice_job_text = text.Text("fonts/COMIC.TTF", 30, f"Level {level_num-1} Complete!", (255,255,255), 250, 100)
    continue_txt = "Click Anywhere to Continue to Next Level" if level_num < 4 else "Click Anywhere to Continue"
    continue_text = text.Text("fonts/COMIC.TTF", 20, continue_txt, (255,255,255), 250, 525)
    level_tries_text = text.Text("fonts/COMIC.TTF", 25, f"Attempts: {level_tries}", (255,255,255), 250, 200)
    level_time_text = text.Text("fonts/COMIC.TTF", 25, f"Time: {minutes} {seconds}", (255,255,255), 250, 250)
    
    stars = img.imgDisplay((125,165), (188,175), f"menu_buttons/{str(level_status[f"lvl{level_num-1}_stars"])}stars.png")
    
    # Loop variables
    quit = False
    run = True
    while run:
        # Event handles
        clock.tick(FPS)
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
        pygame.draw.rect(SCREEN, (255, 255, 255), (50, 175, 400, 100), 1)
        nice_job_text.blit_text(SCREEN)
        continue_text.blit_text(SCREEN)
        level_tries_text.blit_text(SCREEN)
        level_time_text.blit_text(SCREEN)
        SCREEN.blit(stars.image, (stars.rect.x, stars.rect.y))
        display_flies.update()
        display_flies.draw(SCREEN)

        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    
    await h.fade_out_animation(clock)
    
    return "quit" if quit else "continue"