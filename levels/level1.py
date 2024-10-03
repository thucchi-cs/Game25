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
                if event.key == pygame.K_l:
                    run = False

                # Press button
                if event.key == pygame.K_SPACE:
                    fly.stuck = False
                    button1.press()
        
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

        # Draw on screen
        SCREEN.fill((255,255,255))
        walls.draw(SCREEN)
        players.draw(SCREEN)
        buttons.draw(SCREEN)
        webs.draw(SCREEN)
        gates.draw(SCREEN)

        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit