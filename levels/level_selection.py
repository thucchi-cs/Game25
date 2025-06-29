# Libraries imports
import asyncio
import pygame
import sprites.menuButtons as btn
import sprites.images as img
from constants import *
import levels.helpers as h

# Level 1 loop
async def menu():
    # Time
    clock = pygame.time.Clock()
    run = True
    quit = False

    # Create buttons
    tut_option = btn.menuBtn((200, 75), (WIDTH//2, HEIGHT // 2+230), f'tutorial{level_status["tutorial"]}.png')
    l1_option = btn.menuBtn((125, 125), (75, HEIGHT // 2 + 70), f'lvl1{level_status["lvl1"]}.png')
    l2_option = btn.menuBtn((125, 125), (WIDTH // 2, HEIGHT // 2 + 70), f'lvl2{level_status["lvl2"]}.png')
    l3_option = btn.menuBtn((125, 125), (WIDTH - 75, HEIGHT // 2 + 70), f'lvl3{level_status["lvl3"]}.png')

    # Stars
    l1_stars = img.imgDisplay((125,165), (13,308), "menu_buttons/0stars.png")
    l2_stars = img.imgDisplay((125,165), (188,308), "menu_buttons/0stars.png")
    l3_stars = img.imgDisplay((125,165), (363,308), "menu_buttons/0stars.png")

    dirt = img.imgDisplay((1200,1200),(0,0),'menu_assets/dirt.jpg')
    dirt2 = img.imgDisplay((1200,1200),(0,-1200),'menu_assets/dirt.jpg')

    player_text = img.imgDisplay((500,600),(0,0),'menu_assets/select_level.png')

    
    # Button sprite group
    btns = pygame.sprite.Group()
    bg = pygame.sprite.Group()
    bg.add(dirt,dirt2)
    layer1 = pygame.sprite.Group()

    btns.add(l1_option, l2_option, l3_option, tut_option)
    layer1.add(player_text, l1_stars, l2_stars, l3_stars)

    level = 1
    
    fade = 255

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
            
            # Check if button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If choose 2 players
                if l1_option.is_clicked():
                    level = 1
                    run=False
                # If choose 3 players
                elif l2_option.is_clicked():
                    level = 2
                    run=False
                # If choose 4 players
                elif l3_option.is_clicked():
                    level = 3
                    run=False
                elif tut_option.is_clicked():
                    level = 0
                    run = False

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
        fade = h.fade_in_animation(fade)

        pygame.display.flip()

        # asyncio
        await asyncio.sleep(0)
        
    await h.fade_out_animation(clock)
    return "quit" if quit else ("continue",level)