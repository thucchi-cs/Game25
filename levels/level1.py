# Libraries imports
import asyncio
import pygame

# Level 1 loop
async def level(people, guy, girl, SCREEN):
    clock = pygame.time.Clock()
    FPS = 40
    run = True

    while run:
        clock.tick(FPS)

        # Event handles
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        # Move sprites
        key = pygame.key.get_pressed()
        guy.move_arrows(key)
        girl.move_wasd(key)

        # Draw on screen
        SCREEN.fill((255,255,255))
        people.draw(SCREEN)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)