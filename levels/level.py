# Libraries imports
import asyncio
import pygame
# from constants import *
import globals
import sprites.images as img
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
    skip = 0
    for sprite in globals.all:
        sprite.rect.y += skip
    for e in globals.elevators:
        e.dest += skip
        e.start += skip
    for f in globals.frogs:
        f.pos = (f.pos[0], f.pos[1]+skip)
    zero_pos += skip
    dirt = img.imgDisplay((1200,1200),(0,0),'menu_assets/dirt.jpg')
    dirt2 = img.imgDisplay((1200,1200),(0,-1200),'menu_assets/dirt.jpg')
    bg = pygame.sprite.Group()
    bg.add(dirt,dirt2)
    # constants.all.add(bg)
        
    # Level loop
    while run:
        clock.tick(globals.FPS)
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
                    # Unlock next level if currently playing on the newest level and final level hasn't been unlocked
                    levels_unlocked = globals.player_data.get("levels_unlocked")
                    if levels_unlocked < globals.num_of_levels and lvl == levels_unlocked:
                        globals.player_data.update({"levels_unlocked":levels_unlocked+1})
                    # Update the stars collected
                    stars_update = globals.player_data.get(f"level{lvl}_stars")
                    for star in globals.stars_collected.sprites():
                        stars_update[star.id-1] = 1
                    globals.player_data.update({f"level{lvl}_stars":stars_update})
                    # Update the database if the player is signed in
                    if globals.player_signed_in:
                        globals.supabase.table("player_progress").update(globals.player_data).eq("player_name", globals.player_username).execute()
                    run = False
                    
                # Stop scroll cheat code
                if event.key == pygame.K_BACKSPACE:
                    globals.SPEED = 0 if globals.SPEED else 1
              
        # Win level   
        if h.check_win():
            # Unlock next level if currently playing on the newest level and final level hasn't been unlocked
            levels_unlocked = globals.player_data.get("levels_unlocked")
            if levels_unlocked < globals.num_of_levels and lvl == levels_unlocked:
                globals.player_data.update({"levels_unlocked":levels_unlocked+1})
            # Update the stars collected
            stars_update = globals.player_data.get(f"level{lvl}_stars")
            for star in globals.stars_collected.sprites():
                stars_update[star.id-1] = 1
            globals.player_data.update({f"level{lvl}_stars":stars_update})
            # Update the database if the player is signed in
            if globals.player_signed_in:
                globals.supabase.table("player_progress").update(globals.player_data).eq("player_name", globals.player_username).execute()
            run = False
        
        # Move sprites and interact with other elements
        if len(dead_flys) == 0:
            save_display = False
            for fly in globals.players:
                dead = fly.collide_rock(globals.rocks) or fly.check_dead_obstacles(pygame.sprite.Group(globals.lasers, globals.frogs)) or fly.check_offscreen()
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
            if globals.ends.sprites()[0].rect.y < 0:
                scroll = h.auto_scroll(counter,dirt,dirt2)
            h.load_on_screen()
        else:
            if counter - start_dead < 40:
                for fly in dead_flys:
                    fly.flash()
            else:
                restart = True
                run = False
        last_sprite = globals.all.sprites()[-1]
        # zero_pos += constants.SPEED + addition if scroll else 0
        coor = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]-zero_pos)
        print(coor)
        # Draw on screen




        # step = 50
        # for i in range(step, constants.WIDTH, step):
        #     pygame.draw.line(constants.SCREEN, (255, 0, 0), (i, 0), (i, constants.HEIGHT))
        # for i in range(step, constants.HEIGHT, step):
        #     pygame.draw.line(constants.SCREEN, (0, 0, 255), (0, i), (constants.WIDTH, i))
        # pygame.draw.line(constants.SCREEN, (0, 255, 0), (constants.WIDTH // 2, 0), (constants.WIDTH // 2, constants.HEIGHT), width = 2)
        # pygame.draw.line(constants.SCREEN, (0, 255, 0), (0, constants.HEIGHT // 2), (constants.WIDTH, constants.HEIGHT // 2), width = 2)
        bg.draw(globals.SCREEN)
        globals.all.draw(globals.SCREEN)
        if save_display:
            globals.save_text.blit_text(globals.SCREEN)
        globals.all.update()
        globals.key_counter.draw(globals.SCREEN)
        if len(globals.stars_collected) > 0:
            globals.stars_collected.draw(globals.SCREEN)
        
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
    # h.fade_out_animation(clock)
    
    globals.all.remove(bg)
    
    # end
    if quit:
        return "quit"
    elif restart:
        return "restart"
    else:
        return "win"
