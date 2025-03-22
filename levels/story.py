# Libraries imports
import asyncio
import pygame
# from constants import *
import constants
import sprites.storyboard as storyboard_sprite
import levels.helpers as h
import sprites.text as txt

# Level 3 loop
async def storyboard():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False
    counter = 0
    board = storyboard_sprite.StoryBoard()
    gliding = True
    fade = 255
    
    text = txt.Text("fonts/COMICBD.TTF", 30, "PRESS SPACE TO SKIP", (200,200,200), 250, 30)
    text_on = False
    text_count = 0
        
    # Level loop
    while run:
        clock.tick(constants.FPS)
        counter += 1

        # Event handles
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    quit = True
                
                # Check to skip level
                if event.key == pygame.K_TAB:
                    run = False
                    
                if event.key == pygame.K_SPACE and text_on:
                    run = False
                
                text_on = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                text_on = True
                        
        if counter % 100 == 0:
            gliding = False
            if board.curr_pt == len(board.stop_points) -1:
                run = False
        elif not gliding:
            gliding = board.glide((board.curr_pt+1) % len(board.stop_points))
            
                
        board.draw()
        if text_on:
            text_count += 1
            text.blit_text(constants.SCREEN)
            if text_count % 80 == 0:
                text_count = 0
                text_on = False
        fade = h.fade_in_animation(fade)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
        
    await h.fade_out_animation(clock)
        
    # end
    if quit:
        return "quit"
    else:
        return "win"
