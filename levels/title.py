# Libraries imports
import asyncio
import pygame
import pygame.examples
import sprites.menuButtons as btn
import sprites.images as img
from constants import *
import levels.player_selection as player_selection

# Level 1 loop
async def menu():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False

    # Create buttons
    p2_option = btn.menuBtn((125, 125), (75, HEIGHT // 2 + 150), 'player2button.png')
    p3_option = btn.menuBtn((125, 125), (WIDTH // 2, HEIGHT // 2 + 150), 'player3button.png')
    p4_option = btn.menuBtn((125, 125), (WIDTH - 75, HEIGHT // 2 + 150), 'player4button.png')
    load_game_btn = btn.menuBtn((50, 50), (250, 475), 'yes_button.png')
    new_game_btn = btn.menuBtn((50, 50), (250, 525), 'no_button.png')
    save_data_btn = btn.menuBtn((50, 50), (250, 250), 'yes_button.png')
    guest_btn = btn.menuBtn((50, 50), (250, 350), 'no_button.png')

    # Create Assets
    menu_text = img.imgDisplay((500,600),(0,0),'menu_assets/fly_out_text.png')

    dirt1y = 0
    dirt2y = 1200
    flyxs = 75
    flyys = 100
    dirt = img.imgDisplay((1200,1200),(0,0),'menu_assets/dirt.jpg')
    dirt2 = img.imgDisplay((1200,1200),(0,-1200),'menu_assets/dirt.jpg')

    player_text = img.imgDisplay((500,600),(0,0),'menu_assets/player_name.png')

    # Static Flies

    fly1menu = img.imgDisplay((flyxs,flyys),(45,275),'fly1.1.png',1)
    fly2menu = img.imgDisplay((flyxs,flyys),(159,290),'fly2.1.png',2)
    fly3menu = img.imgDisplay((flyxs,flyys),(271,305),'fly3.1.png',3)
    fly4menu = img.imgDisplay((flyxs,flyys),(382,320),'fly4.1.png',4)

    
    # Button sprite group
    btns = pygame.sprite.Group()
    btns.add(new_game_btn, load_game_btn)
    bg = pygame.sprite.Group()
    bg.add(dirt,dirt2)
    layer1 = pygame.sprite.Group()
    layer1.add(menu_text,fly1menu,fly2menu,fly3menu,fly4menu)


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    quit = True
                if event.key == pygame.K_TAB:
                    players.remove(fly3,fly4)
                    all.remove(fly3,fly4)
                    run=False
            
            # Check if button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if load_game_btn.is_clicked():
                    btns.remove(load_game_btn, new_game_btn)
                    layer1.remove(menu_text,fly1menu,fly2menu,fly3menu,fly4menu)
                    layer1.add(player_text)
                    btns.add(p2_option, p3_option, p4_option)
                    await player_selection.enter_player()
    
                elif new_game_btn.is_clicked():
                    btns.remove(load_game_btn, new_game_btn)
                    btns.add(guest_btn, save_data_btn)
                    layer1.remove(menu_text,fly1menu,fly2menu,fly3menu,fly4menu)

                elif save_data_btn.is_clicked():
                    btns.add(p2_option, p3_option, p4_option)
                    btns.remove(guest_btn, save_data_btn)
                    layer1.remove(menu_text,fly1menu,fly2menu,fly3menu,fly4menu)
                    layer1.add(player_text)
                    await player_selection.create_player()

                elif guest_btn.is_clicked():
                    btns.add(p2_option, p3_option, p4_option)
                    btns.remove(guest_btn, save_data_btn)
                    layer1.remove(menu_text,fly1menu,fly2menu,fly3menu,fly4menu)
                    layer1.add(player_text)
                
                # If choose 2 players
                elif p2_option.is_clicked():
                    players.remove(fly3,fly4)
                    all.remove(fly3,fly4)
                    run=False
                # If choose 3 players
                elif p3_option.is_clicked():
                    players.remove(fly4)
                    all.remove(fly4)
                    run=False
                # If choose 4 players
                elif p4_option.is_clicked():
                    run=False


        fly1menu.animate_fly()
        fly2menu.animate_fly()
        fly3menu.animate_fly()
        fly4menu.animate_fly()
        # Infinite Background

        if dirt.rect.y <=1200:
            dirt.move_up()
            dirt2.move_up()
        else:
            dirt.rect.y = dirt2.rect.y - 1200

        if dirt2.rect.y <=1200:
            dirt.move_up()
            dirt2.move_up()
        else:
            dirt2.rect.y = dirt.rect.y - 1200
        
            

        # Draw on screen


        SCREEN.fill((255,255,255))
        bg.draw(SCREEN)
        layer1.draw(SCREEN)
        btns.draw(SCREEN)

        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
    
    return "quit" if quit else "continue"