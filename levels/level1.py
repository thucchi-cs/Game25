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
    counter = 0

    h.load_layout('level1.json')

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
        if len(players.sprites()) == 0:
            print('GAME OVER')
        
        # Move sprites and interact with other elements
        key = pygame.key.get_pressed() 
        h.move_players(key)
        save_display = False
        for fly in players:
            dead = fly.collide_rock(rocks) or fly.check_lasers(lasers)
            
            if fly.stuck:
                save_display = True
            if fly.check_end(ends):

                players.remove(fly)
                all.remove(fly)



        # Debug prints
        # print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y),'Dead' if fly.collide_rock(rocks) else 'Alive', water1.counter,water1.counter2, water1.rect.x )
        # print(dead)

        # Auto Scroll
        h.auto_scroll(counter)

        # Draw on screen
        SCREEN.fill((255,255,255))
        all.draw(SCREEN)
        if save_display:
            save_text.blit_text(SCREEN)
        txt.blit_text(SCREEN)
        all.update()
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit