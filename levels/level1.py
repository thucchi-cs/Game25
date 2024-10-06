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
                if event.key == pygame.K_TAB:
                    run = False

                # Press button
                if event.key == pygame.K_SPACE:
                    fly.stuck = False
                    pressed = button1.press(lasers, elevators)
        
        # Check for web collision
        for fly in players:
            fly.check_web(webs)

        # Move sprites
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            fly.stuck = False
    
        if not fly.stuck:
            fly.move_arrows(key, walls, gates)
        
        # Open gate if button pressed
        if button1.pressed and not gate1.open:
            gate1.unlock()
        elif not button1.pressed and not gate1.closed:
            gate1.lock()

        print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y),'Dead' if fly.collide_rock(rocks) else 'Alive', water1.counter,water1.counter2, water1.rect.x )

        # interact flies with obstacles
        fly.elevator_move(elevators)
        rock1.check_line()
        water1.animate(pressed)
        rock1.remove
        water1.water_button_pressed(pressed)
        
        # Draw on screen
        SCREEN.fill((255,255,255))
        lasers.update()
        elevators.update()
        all.draw(SCREEN)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit