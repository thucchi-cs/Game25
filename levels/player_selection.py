import asyncio
import constants
from constants import *
from sprites.text import Text
import sprites.menuButtons as btn
import pygame

# Text variables
first_time_text = Text("fonts/COMIC.ttf", 15, f"If this is your first time playing, click here to create an account", (255,255,255), 250, 450)
create_id_text = Text("fonts/COMIC.ttf", 30, f"Create a Username", (255,255,255), 250, 200)
enter_id_text = Text("fonts/COMIC.ttf", 30, f"Enter Your Username", (255,255,255), 250, 200)
unique_id_text = Text("fonts/COMIC.ttf", 30, f"Player Name Already Exists", (255,255,255), 250, 400)
does_not_exist_text = Text("fonts/COMIC.ttf", 30, f"Player Does Not Exist", (255,255,255), 250, 400)

# Buttons
create_btn = btn.menuBtn((50, 50), (250, 500), 'yes_button.png')

# Player username input text box and text
input_box = pygame.Rect(70, 300, 360, 50)
username =  Text("fonts/COMIC.ttf", 30, f"", (255,255,255), 250, 325)

async def select_player():
    # Boolean variables determine what text to display
    creating_username = False
    entering_username = True
    unique_id_display = False
    does_not_exist_display = False
    run = True
    quit = False
    while run:
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            # Check if button is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the create account button is clicked, switch from entering to creating username
                if create_btn.is_clicked():
                    creating_username = True
                    entering_username = False
            # Update username every time a key is clicked
            elif event.type == pygame.KEYDOWN:
                # Backspace
                if event.key == pygame.K_BACKSPACE and len(username.text) >= 0:
                    username.text = username.text[:-1]
                # Check if enter is clicked and creating username
                elif event.key == pygame.K_RETURN and len(username.text) > 0  and creating_username:
                    # If the username entered already exists, display a wanring letting the user know
                    if player_database.contains(Player.username == username.text):
                        unique_id_display = True
                    # If the username does not exist, add it to the player database and set it as the current player username
                    else:
                        player_database.insert({'username':username.text, 'level1':{'unlocked':True, 'completed':False, 'star1':False, 'star2':False, 'star3':False}, 'level2':{'unlocked':False, 'completed':False, 'star1':False, 'star2':False, 'star3':False}, 'level3':{'unlocked':False, 'completed':False, 'star1':False, 'star2':False, 'star3':False}})
                        constants.player_username = username.text
                        constants.player = player_database.get(Player.username == constants.player_username)
                        run = False
                # Check if enter is clicked and entering username
                elif event.key == pygame.K_RETURN and len(username.text) > 0  and entering_username:
                    # If the username entered does not exist, display a wanrning letting the user know
                    if not player_database.contains(Player.username == username.text):
                        does_not_exist_display = True
                    # If the username does exist, set it as the current player username
                    else:
                        constants.player_username = username.text
                        constants.player = player_database.get(Player.username == constants.player_username)
                        run = False
                elif len(username.text) < 12:
                    username.text += event.unicode
        SCREEN.fill((0,0,0))

        # Display entering username screen
        if entering_username:
            enter_id_text.blit_text(SCREEN)
            pygame.draw.rect(SCREEN, (200, 200, 200), input_box, 2)
            username.blit_text(SCREEN)
            first_time_text.blit_text(SCREEN)
            SCREEN.blit(create_btn.image, (225, 475))
        # Display creating username screen
        else:
            create_id_text.blit_text(SCREEN)
            pygame.draw.rect(SCREEN, (200, 200, 200), input_box, 2)
            username.blit_text(SCREEN)
        
        # Display unique ID warning if necessary
        if unique_id_display:
            unique_id_text.blit_text(SCREEN)

        # Display non-existing player warning if necessary
        if does_not_exist_display:
            does_not_exist_text.blit_text(SCREEN)

        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    return "quit" if quit else "continue"
