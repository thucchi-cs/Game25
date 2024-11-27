# Libraries imports
import asyncio
import pygame
from constants import *
import levels.helpers as h
# Level 1 loop
async def level():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False
    dead = False
    mainmenu = True
    playermenu = False

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
                if event.key == pygame.K_TAB:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint:
                    mainmenu = False
                    playermenu = True
                if preplayer2_rect.collidepoint:
                    playercount = 2
                    players.remove(fly3,fly4)
                    all.remove(fly3,fly4)
                    run=False
                elif preplayer3_rect.collidepoint:
                    playercount=3
                    players.remove(fly4)
                    all.remove(fly4)
                    run=False
                elif preplayer4_rect.collidepoint:
                    run=False
                
                # Check to skip level


        
        # Move sprites and interact with other elements




        # Debug prints
        # print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y),'Dead' if fly.collide_rock(rocks) else 'Alive', water1.counter,water1.counter2, water1.rect.x )
        # print(dead)

        # Auto Scroll

        # Draw on screen
        SCREEN.fill((255,255,255))
        
       
        # BUTTON W/H = 1397 WIDTH, 470 HEIGHT. 2.972:1 RATIO
        prestart = pygame.image.load('graphics/menu_buttons/Start-Game.png')
        start_button=pygame.transform.scale(prestart,(279,94))
        start_button_rect = start_button.get_rect()
        start_button_rect.center = (WIDTH // 2, HEIGHT // 2)

        preplayer2 = pygame.image.load('graphics/menu_buttons/2-player-button.png')
        preplayer3 = pygame.image.load('graphics/menu_buttons/3-player-button.png')
        preplayer4 = pygame.image.load('graphics/menu_buttons/4-player-button.png')
        preplayer2_rect = preplayer2.get_rect()
        preplayer2_rect.center=((WIDTH-WIDTH)+75,HEIGHT//2+150) 
        preplayer3_rect = preplayer2.get_rect()
        preplayer3_rect.center=(WIDTH//2,HEIGHT//2+150)        
        preplayer4_rect = preplayer2.get_rect()
        preplayer4_rect.center=(WIDTH-75,HEIGHT//2+150)

        if mainmenu:
            SCREEN.blit(start_button,start_button_rect)
        elif playermenu:
            SCREEN.blit(preplayer2,preplayer2_rect)
            SCREEN.blit(preplayer3,preplayer3_rect)
            SCREEN.blit(preplayer4,preplayer4_rect)
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit