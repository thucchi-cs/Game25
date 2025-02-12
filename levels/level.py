# Libraries imports
import asyncio
import pygame
# from constants import *
import constants
import levels.helpers as h
import threading


# Level loop
async def level(lvl):
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False
    dead_flys = []
    counter = 0
    zero_pos = 0
    start_dead = 0
    restart = False
    fade = 255
    h.load_layout('level'+str(lvl)+'.json')

    # 159 390
    skip = 0
    for sprite in constants.all:
        sprite.rect.y += skip
    for e in constants.elevators:
        e.dest += skip
        e.start += skip
    for f in constants.frogs:
        f.pos = (f.pos[0], f.pos[1]+skip)
    zero_pos += skip
    
    # Add the players back into all
    constants.all.add(constants.players)

    # Level loop
    while run:
        clock.tick(constants.FPS)
        counter += 1
        # if counter % 2 == 0:
        #     h.something()

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
                    
                # Stop scroll cheat code
                if event.key == pygame.K_BACKSPACE:
                    constants.SPEED = 0 if constants.SPEED else 1
              
        # Win level   
        if h.check_win():
            constants.player[f"level{lvl}"]["completed"] = True
            if lvl < 3:
                constants.player[f"level{lvl+1}"]["unlocked"] = True
            run = False   
        
        # Move sprites and interact with other elements
        if len(dead_flys) == 0:
            save_display = False
            for fly in constants.players:
                dead = fly.collide_rock(constants.rocks) or fly.check_lasers(constants.lasers) or fly.check_offscreen()
                if dead:
                    dead_flys.append(fly)
                    start_dead = counter
                # Check for web collision
                if fly.stuck:
                    save_display = True
            # Debug prints
            # print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y),'Dead' if fly.collide_rock(rocks) else 'Alive', water1.counter,water1.counter2, water1.rect.x )
        
            key = pygame.key.get_pressed() 
            h.move_players(key)
            # Auto Scroll
            scroll = h.auto_scroll(counter)
            h.load_on_screen()
        else:
            if counter - start_dead < 40:
                for fly in dead_flys:
                    fly.flash()
            else:
                restart = True
                run = False
        last_sprite = constants.all.sprites()[-1]
        zero_pos += constants.SPEED if scroll else 0
        # coor = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]-zero_pos)
        # print(coor)
        # Draw on screen
        constants.SCREEN.fill((92, 64, 51))



        # step = 50
        # for i in range(step, constants.WIDTH, step):
        #     pygame.draw.line(constants.SCREEN, (255, 0, 0), (i, 0), (i, constants.HEIGHT))
        # for i in range(step, constants.HEIGHT, step):
        #     pygame.draw.line(constants.SCREEN, (0, 0, 255), (0, i), (constants.WIDTH, i))
        # pygame.draw.line(constants.SCREEN, (0, 255, 0), (constants.WIDTH // 2, 0), (constants.WIDTH // 2, constants.HEIGHT), width = 2)
        # pygame.draw.line(constants.SCREEN, (0, 255, 0), (0, constants.HEIGHT // 2), (constants.WIDTH, constants.HEIGHT // 2), width = 2)
        
        constants.all.draw(constants.SCREEN)
        if save_display:
            constants.save_text.blit_text(constants.SCREEN)
        constants.all.update()
        fade = h.fade_in_animation(fade)
        
        pygame.display.flip()
        # h.fade_animation(clock, h.fade_in, 255)
        # print(len(constants.all))

        # asyncio
        await asyncio.sleep(0)
        
    # restart message
    if restart:
        h.restart_transition(clock)
    
    # fade out
    h.fade_out_animation(clock)
    
    # end
    if quit:
        return "quit"
    elif restart:
        return "restart"
    else:
        return "win"
