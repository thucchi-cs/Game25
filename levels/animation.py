# Libraries imports
import asyncio
import pygame
from constants import *
import levels.helpers as h
import sprites.images as img
import sprites.curve as curve

# Animation loop
async def animation():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False
    
    logo = img.imgDisplay((500,600),(0,0),'menu_assets/fly_out_text.png')

    fly_size = (40, 60)
    fly1 = img.imgDisplay(fly_size,(230,600),'fly1.1.png',1)
    fly2 = img.imgDisplay(fly_size,(64,1500),'fly2.1.png',2)
    fly3 = img.imgDisplay(fly_size,(230,1500),'fly3.1.png',3)
    fly4 = img.imgDisplay(fly_size,(396,1500),'fly4.1.png',4)

    flies = pygame.sprite.Group(fly1, fly2, fly3, fly4)
    for fly in flies.sprites():
        fly.speed = 10

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

        fly1.glide_to((230, -200))
        fly2.glide_to((64, -200))
        fly3.glide_to((230, -200))
        fly4.glide_to((396, -200))

        for fly in flies.sprites():
            fly.animate_fly()

        # Draw on screen
        SCREEN.fill((0,0,0))
        logo.draw(SCREEN)

        # Cover box
        pygame.draw.polygon(SCREEN, (0,0,0), [(0,0), (0, fly2.rect.bottom),fly3.rect.bottomleft, (500,fly4.rect.bottom),(500,0)])

        # Flies
        flies.draw(SCREEN)

        pygame.display.flip()

        for fly in flies.sprites():
            if fly.rect.bottom > -100:
                break
        else:
            run = False

        # asyncio
        await asyncio.sleep(0)
        
    return "quit" if quit else "continue"