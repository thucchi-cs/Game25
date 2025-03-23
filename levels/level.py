# Libraries imports
import asyncio
import pygame
# from constants import *
import constants
import sprites.images as img
import levels.helpers as h
import sprites.pause as p
import time
import math

# Level loop
async def level(lvl):
    # Time
    start_time = time.time()
    clock = pygame.time.Clock()
    pygame.mixer.init()
    run = True
    quit = False
    dead_flys = []
    counter = 0
    zero_pos = 0
    start_dead = 0
    dead = False
    restart = False
    paused = False
    psc = False
    fade = 255
    main_menu = False
    scroll = False

    deadSound = pygame.mixer.Sound("music/death.ogg")
    deadPlayed = False
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
    dirt = img.imgDisplay((1200,1200),(0,0),'menu_assets/dirt.jpg')
    dirt2 = img.imgDisplay((1200,1200),(0,-1200),'menu_assets/dirt.jpg')
    pause1 = img.imgDisplay((500,600),(0,0),'dummy_do_is_a_dummy.png')
    pause = p.Pause()
    bg = pygame.sprite.Group()
    bg.add(dirt,dirt2)
    fg = pygame.sprite.Group()
    fg.add(pause)
    ps = pygame.sprite.Group()
    ps.add(pause1)
    
    lvltxt = img.imgDisplay((250, 40), (125, 550), f"nnnlvl{lvl}txt.png")
    constants.all.add(lvltxt)
    
    # constants.all.add(bg)
        
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
                # if event.key == pygame.K_q:
                #     run = False
                #     quit = True
                # pass
                
                # Check to skip level
                if event.key == pygame.K_TAB:
                    if paused == False:
                        paused = True
                    else:
                        paused = False
                    
                # Stop scroll cheat code
                # if event.key == pygame.K_BACKSPACE:
                    

                #     constants.SPEED = 0 if constants.SPEED else 1
                # if event.key == pygame.K_END:
                #     run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if h.onButton("pause") and paused == False:
                    paused = True

                if paused == True and h.onButton("continue"):
                    paused = False
                if paused == True and h.onButton("restart"):
                    run = False
                    restart = True
                if paused == True and h.onButton("main"):
                    run = False
                    main_menu = True
              
        # Win level   
        if h.check_win():
            run = False 
        h.isWater()     
        # h.isFrog()   
        # Move sprites and interact with other elements
        if len(dead_flys) == 0 and paused == False:
            all_stuck = True
            save_display = False
            for fly in constants.players:
                dead = fly.collide_rock(constants.rocks) or fly.check_dead_obstacles(pygame.sprite.Group(constants.lasers, constants.frogs)) or fly.check_offscreen()
                if dead:
                    dead_flys.append(fly)
                    start_dead = counter
                # Check for web collision
                if fly.stuck:
                    save_display = True
                else:
                    all_stuck = False
            # Debug prints
            # print((fly.realX,fly.realY),int(fly.rise), (rock1.actualLY,rock1.actualRY),rock1.counter,(rock1.actualRY,rock1.rect.y),'Dead' if fly.collide_rock(rocks) else 'Alive', water1.counter,water1.counter2, water1.rect.x )
        
            key = pygame.key.get_pressed() 
            if key[pygame.K_LSHIFT] and key[pygame.K_END]:
                run = False
            h.move_players(key)
            # Auto Scroll
            if constants.ends.sprites()[0].rect.y < 0 and counter > 50:
                scroll = h.auto_scroll(counter,dirt,dirt2)
            h.load_on_screen()
            psc = False
        elif len(dead_flys) > 0:
            if deadPlayed == False:
                pygame.mixer.Sound.set_volume(deadSound,0.4)
                pygame.mixer.Sound.play(deadSound)
                deadPlayed = True
            psc = False
            if counter - start_dead < 40:
                for fly in dead_flys:
                    fly.flash()
            else:
                dead = True
                run = False
        elif paused == True:
            psc = True

        if all_stuck:
            if deadPlayed == False:
                pygame.mixer.Sound.set_volume(deadSound,0.4)
                pygame.mixer.Sound.play(deadSound)
                deadPlayed = True
            print('last')
            dead = True
            run = False
            
            


        last_sprite = constants.all.sprites()[-1]
        zero_pos += constants.SPEED if scroll else 0
        coor = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]-zero_pos)
        # print(coor)
        # Draw on screen




        # step = 50
        # for i in range(step, constants.WIDTH, step):
        #     pygame.draw.line(constants.SCREEN, (255, 0, 0), (i, 0), (i, constants.HEIGHT))
        # for i in range(step, constants.HEIGHT, step):
        #     pygame.draw.line(constants.SCREEN, (0, 0, 255), (0, i), (constants.WIDTH, i))
        # pygame.draw.line(constants.SCREEN, (0, 255, 0), (constants.WIDTH // 2, 0), (constants.WIDTH // 2, constants.HEIGHT), width = 2)
        # pygame.draw.line(constants.SCREEN, (0, 255, 0), (0, constants.HEIGHT // 2), (constants.WIDTH, constants.HEIGHT // 2), width = 2)
        bg.draw(constants.SCREEN)

        constants.all.draw(constants.SCREEN)
        constants.key_counter.draw(constants.SCREEN)

        if save_display:
            constants.save_text.blit_text(constants.SCREEN)
            
        fg.draw(constants.SCREEN)
        if psc == True:
            print(dead)
            ps.draw(constants.SCREEN)

        constants.all.update()
        fade = h.fade_in_animation(fade)
        
        pygame.display.flip()
        # h.fade_animation(clock, h.fade_in, 255)
        # print(len(constants.all))

        # asyncio
        await asyncio.sleep(0)
        
    # restart message
    # if restart:
    #     h.restart_transition(clock)
    
    # fade out
    # await h.fade_out_animation(clock)
    
    constants.all.remove(bg)
    
    # end
    end_time = time.time()
    level_time = end_time - start_time
    if quit:
        return "quit", math.floor(level_time)
    elif dead:
        return "dead", math.floor(level_time)
    elif restart:
        await h.fade_out_animation(clock)
        return "restart", math.floor(level_time)
    elif main_menu:
        await h.fade_out_animation(clock)
        return "menu", math.floor(level_time)
    else:
        return "win", math.floor(level_time)
