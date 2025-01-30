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
    zero_pos = 0
    h.load_layout('level2.json')
    for sprite in all:
        sprite.rect.y +=100
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
            run = False
        
        # Move sprites and interact with other elements
        key = pygame.key.get_pressed() 
        h.move_players(key)
        save_display = False
        for fly in players:
            dead = fly.collide_rock(rocks) or fly.check_lasers(lasers)
            # Check for web collision
            if fly.stuck:
                save_display = True

        # Debug prints
        # print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y),'Dead' if fly.collide_rock(rocks) else 'Alive', water1.counter,water1.counter2, water1.rect.x )
        # print(dead)

        # Auto Scroll
        scroll = h.auto_scroll(counter)

        # zero_pos += SPEED if scroll else 0
        # coor = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]-zero_pos)
        # print(coor)
        # Draw on screen
        SCREEN.fill((92, 64, 51))



        step = 50
        for i in range(step, WIDTH, step):
            pygame.draw.line(SCREEN, (255, 0, 0), (i, 0), (i, HEIGHT))
        for i in range(step, HEIGHT, step):
            pygame.draw.line(SCREEN, (0, 0, 255), (0, i), (WIDTH, i))
        pygame.draw.line(SCREEN, (0, 255, 0), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), width = 2)
        pygame.draw.line(SCREEN, (0, 255, 0), (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), width = 2)
        mouse_pos = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

        last_sprite = all.sprites()[-1]
        print(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]-100)


        if str(last_sprite).startswith("<Buttons") or str(last_sprite).startswith("<Web"):
            print("Center Center object found")
            last_sprite.rect.centerx = mouse_pos[0]
            last_sprite.rect.centery = mouse_pos[1]
        elif str(last_sprite).startswith("<Wall") or str(last_sprite).startswith("<Gate") or str(last_sprite).startswith("<Water") or str(last_sprite).startswith("<Rocks"):
            print("Top left found")
            last_sprite.rect.x = mouse_pos[0]
            last_sprite.rect.y = mouse_pos[1]
        elif str(last_sprite).startswith("<Lasers") or str(last_sprite).startswith("<Elevators"):
            print("Center Top found")
            last_sprite.rect.centerx = mouse_pos[0]
            last_sprite.rect.y = mouse_pos[1]
        all.draw(SCREEN)

        


        
        if save_display:
            save_text.blit_text(SCREEN)
        all.update()
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return quit