# Libraries imports
import asyncio
import pygame
# from constants import *
import constants
import sprites.images as img
import levels.helpers as h
import sprites.pause as p
import sprites.menuButtons as btns

# Level 3 loop
async def level():
    # Time
    clock = pygame.time.Clock()
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
    h.load_layout('tutorial.json')
    
    web_directions = img.imgDisplay((143, 103), (5, 382), "webDir.png")
    btn_directions = img.imgDisplay((250, 60), (240, 280), "BtnDir.png")
    gate_directions = img.imgDisplay((300, 30), (0, 165), "gateDir.png")
    water_directions = img.imgDisplay((150, 40), (240, 10), "waterDir.png")

    deadSound = pygame.mixer.Sound("music/death.ogg")
    deadPlayed = False
    
    dirt = img.imgDisplay((1200,1200),(0,0),'menu_assets/dirt.jpg')
    pause1 = img.imgDisplay((500,600),(0,0),'dummy_do_is_a_dummy.png')
    pause = p.Pause()
    skipBtn = btns.menuBtn((60, 30), (460, 575), "skipBtn.png")
    bg = pygame.sprite.Group()
    bg.add(dirt)
    fg = pygame.sprite.Group()
    fg.add(pause, skipBtn, web_directions, btn_directions, gate_directions, water_directions)
    ps = pygame.sprite.Group()
    ps.add(pause1)
    
    showing_instructions = True
    instructions = img.imgDisplay((500,600), (0,0), "PlayerControls2.png")
    fg.add(instructions)
    
    for fly in constants.players:
        fly.rect.y = 512
    constants.fly2.rect.topleft = (176, 424)
    
    lvltxt = img.imgDisplay((500, 40), (0, 550), "tutorialtxt.png")
    constants.all.add(lvltxt)
            
    # Level loop
    while run:
        clock.tick(constants.FPS)
        counter += 1

        # Event handles
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            if event.type == pygame.KEYDOWN:
                if showing_instructions:
                    showing_instructions = False
                    fg.remove(instructions)
                
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
                if event.key == pygame.K_BACKSPACE:
                    

                    constants.SPEED = 0 if constants.SPEED else 1
                # if event.key == pygame.K_END:
                #     run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if showing_instructions:
                    showing_instructions = False
                    fg.remove(instructions)
                else:
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
                    
                    if skipBtn.is_clicked():
                        run = False
              
        # Win level   
        if h.check_win():
            run = False 
        
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
            h.move_players(key)
            # Auto Scroll
            if constants.ends.sprites()[0].rect.y < 0 and counter > 50:
                scroll = h.auto_scroll(counter,dirt)
            h.load_on_screen()
            psc = False
        elif len(dead_flys) > 0:
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


        coor = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]-zero_pos)
        print(coor)
        # Draw on screen
        
        bg.draw(constants.SCREEN)

        constants.all.draw(constants.SCREEN)
        if save_display:
            constants.save_text.blit_text(constants.SCREEN)
            
        fg.draw(constants.SCREEN)
        if psc == True:
            ps.draw(constants.SCREEN)

        constants.all.update()
        constants.key_counter.draw(constants.SCREEN)
        fade = h.fade_in_animation(fade)
        
        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    if not dead:
        await h.fade_out_animation(clock)
    constants.all.remove(bg)
    
    # end
    if quit:
        return "quit"
    elif dead:
        return "dead"
    elif restart:
        return "restart"
    elif main_menu:
        return "menu"
    else:
        return "win"
