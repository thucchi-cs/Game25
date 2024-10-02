# Libraries imports
import asyncio
import pygame
from constants import *

# Level 1 loop
async def level():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False
    
    # Level loop
    while run:
        clock.tick(FPS)

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

                # Press button
                if event.key == pygame.K_SPACE:
                    button1.press(lasers, elevators)

        # Move sprites
        key = pygame.key.get_pressed()
        fly.move_arrows(key, walls)

        # interact flies with obstacles
        # print(fly.check_lasers(lasers))
        fly.elevator_move(elevators)

        # Draw on screen
        SCREEN.fill((255,255,255))
        # walls.draw(SCREEN)
        # people.draw(SCREEN)
        # buttons.draw(SCREEN)
        # lasers.draw(SCREEN)
        lasers.update()
        elevators.update()
        all.draw(SCREEN)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit