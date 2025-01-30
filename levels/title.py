# Libraries imports
import asyncio
import pygame
import sprites.menuButtons as btn
from constants import *

# Level 1 loop
async def menu():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False

    # Create buttons
    start_btn = btn.menuBtn((279, 94), (WIDTH // 2, HEIGHT // 2), 'Start-Game.png')
    p2_option = btn.menuBtn((125, 125), (75, HEIGHT // 2 + 150), '2-player-button.png')
    p3_option = btn.menuBtn((125, 125), (WIDTH // 2, HEIGHT // 2 + 150), '3-player-button.png')
    p4_option = btn.menuBtn((125, 125), (WIDTH - 75, HEIGHT // 2 + 150), '4-player-button.png')
    
    # Button sprite group
    btns = pygame.sprite.Group()
    btns.add(start_btn)

    # Menu loop
    while run:
        # Timing
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
                if event.key == pygame.K_TAB:
                    players.remove(fly3,fly4)
                    all.remove(fly3,fly4)
                    run=False
            
            # Check if button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If click start
                if start_btn.is_clicked():
                    # Options to choose number of players
                    btns.add(p2_option, p3_option, p4_option)
                    btns.remove(start_btn)
                
                # If choose 2 players
                elif p2_option.is_clicked():
                    players.remove(fly3,fly4)
                    all.remove(fly3,fly4)
                    run=False
                # If choose 3 players
                elif p3_option.is_clicked():
                    players.remove(fly4)
                    all.remove(fly4)
                    run=False
                # If choose 4 players
                elif p4_option.is_clicked():
                    run=False

        # Draw on screen
        SCREEN.fill((255,255,255))
        btns.draw(SCREEN)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit