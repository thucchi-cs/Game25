# Libraries imports
import asyncio
import pygame
from constants import *

# show grid loop
async def screen():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False

    SCREEN.fill((255,255,255))
    step = 50
    for i in range(step, WIDTH, step):
        pygame.draw.line(SCREEN, (255, 0, 0), (i, 0), (i, HEIGHT))
    for i in range(step, HEIGHT, step):
        pygame.draw.line(SCREEN, (0, 0, 255), (0, i), (WIDTH, i))
    pygame.draw.line(SCREEN, (0, 255, 0), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), width = 2)
    pygame.draw.line(SCREEN, (0, 255, 0), (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), width = 2)

    pygame.display.flip()

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
                    run = False

        # Write coordinates

        # asyncio
        await asyncio.sleep(0)
    
    return quit