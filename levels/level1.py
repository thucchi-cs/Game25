# Libraries imports
import asyncio
import pygame
from constants import *
import helpers as h

# Level 1 loop
async def level():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False
    dead = False
    counter = 0

    # Level loop
    while run:
        clock.tick(FPS)
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

                # Press button
                if event.key == pygame.K_SPACE:
                    fly.stuck = False
                    button1.press(lasers, elevators, waters, gates)
        
        # Move sprites and interact with other elements
        key = pygame.key.get_pressed() 
        h.move_players(key, walls, gates, rocks, waters)
        for fly in players:
            fly.move_arrows(key, walls, gates, rocks, waters)
            fly.elevator_move(elevators)
            fly.check_web(webs)
            dead = fly.collide_rock(rocks) or fly.check_lasers(lasers)
        
        # Debug prints
        print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y),'Dead' if fly.collide_rock(rocks) else 'Alive', water1.counter,water1.counter2, water1.rect.x )
        print(dead)

        # Auto Scroll
        if counter % SPEEDFACTOR == 0:
            for sprite in all:
                sprite.rect.y += SPEED
        
        # Draw on screen
        SCREEN.fill((255,255,255))
        all.draw(SCREEN)
        all.update()
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit