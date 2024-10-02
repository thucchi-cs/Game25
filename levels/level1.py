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
    pressed = False
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
                    pressed = button1.press(waters)

        # Move sprites
        key = pygame.key.get_pressed()
        fly.move_arrows(key, walls,rocks,waters)

        print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y),'Dead' if fly.collide_rock(rocks) else 'Alive', water1.counter,water1.counter2, water1.rect.x )

        rock1.check_line(fly.realY,exclamations)
        water1.animate(pressed)
        rock1.remove
        water1.water_button_pressed(pressed)
        # Draw on screen
        SCREEN.fill((255,255,255))
        walls.draw(SCREEN)
        people.draw(SCREEN)
        buttons.draw(SCREEN)
        rocks.draw(SCREEN)
        exclamations.draw(SCREEN)
        waters.draw(SCREEN)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit