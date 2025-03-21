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
    p2_option = btn.menuBtn((125, 125), (75, HEIGHT // 2 + 150), 'player2button.png')
    p3_option = btn.menuBtn((125, 125), (WIDTH // 2, HEIGHT // 2 + 150), 'player3button.png')
    p4_option = btn.menuBtn((125, 125), (WIDTH - 75, HEIGHT // 2 + 150), 'player4button.png')

    dirt = img.imgDisplay((1200,1200),(0,0),'menu_assets/dirt.jpg')
    dirt2 = img.imgDisplay((1200,1200),(0,-1200),'menu_assets/dirt.jpg')

    player_text = img.imgDisplay((500,600),(0,0),'menu_assets/player_name.png')

    
    # Button sprite group
    btns = pygame.sprite.Group()
    bg = pygame.sprite.Group()
    bg.add(dirt,dirt2)
    layer1 = pygame.sprite.Group()

    btns.add(p2_option, p3_option, p4_option)
    layer1.add(player_text)
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    quit = True
                if event.key == pygame.K_TAB:
                    players.remove(fly3,fly4, fly2)
                    all.remove(fly3,fly4, fly2)
                    run=False
            
            # Check if button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If choose 2 players
                if p2_option.is_clicked():
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
        
    h.fade_out_animation(clock)
    return "quit" if quit else "continue"