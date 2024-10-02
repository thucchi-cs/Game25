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
    passed_line = False
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
                if event.key == pygame.K_l and event.key == pygame.K_COLON:
                    run = False

                # Press button
                if event.key == pygame.K_SPACE:
                    button1.press()

        # Move sprites
        key = pygame.key.get_pressed()
        fly.move_arrows(key, walls,rocks)
        print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y))
        if rock1.check_line(fly.realY):
            rock1.fall_rock()
        # Draw on screen
        SCREEN.fill((255,255,255))
        walls.draw(SCREEN)
        people.draw(SCREEN)
        buttons.draw(SCREEN)
        rocks.draw(SCREEN)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit