# Libraries imports
import asyncio
import pygame
# from constants import *
import constants
import sprites.storyboard as storyboard_sprite
import levels.helpers as h

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
                
                # if event.key == pygame.K_SPACE:
                    # gliding = board.glide(1)
        
        if counter % 100 == 0:
            gliding = False
            if board.curr_pt == len(board.stop_points) -1:
                run = False
        elif not gliding:
            gliding = board.glide((board.curr_pt+1) % len(board.stop_points))
        
        board.draw()
        fade = h.fade_in_animation(fade)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
        
    h.fade_out_animation(clock)
        
    # end
    if quit:
        return "quit"
    else:
        return "win"
