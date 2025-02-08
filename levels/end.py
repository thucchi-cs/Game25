import asyncio
from constants import *
import sprites.text as text
import sprites.flies as flies
import pygame
import levels.helpers as h
import sprites.clouds as cloud

async def End():
    # Get rid of the previous level's obstacles
    h.set_up_end()
    player_count = len(players)
    background = pygame.image.load("graphics/Out1.png")

    clock = pygame.time.Clock()
    run = True
    quit = False
    transition = True
    counter = 0
    
    clouds = pygame.sprite.Group()
    clouds.add(cloud.Cloud((15, 64), 1), cloud.Cloud((302,91), 0.95))
    
    fly1.rect.x = 185
    fly1.rect.y = 470
    fly2.rect.x = 202
    fly2.rect.y = 501
    fly3.rect.x = 113
    fly3.rect.y = 406
    fly4.rect.x = 157
    fly4.rect.y = 439
    fade = 255
    
    while run:
        # Event handles
        clock.tick(FPS)
        counter += 1
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    quit = True

        if counter > FPS//4:
            SCREEN.blit(background, (0,0))
            coor = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
            # print(coor)
            clouds.draw(SCREEN)
            for c in clouds:
                c.move()
            fly1.glide_to((370,371))
            fly2.glide_to((335,461))
            fly3.glide_to((201, 280))
            fly4.glide_to((252,382))
            players.draw(SCREEN)
            players.update()
            fade = h.fade_in_animation(fade)
            pygame.display.flip()
            # asyncio
            await asyncio.sleep(0)
    
    return "quit" if quit else "continue"