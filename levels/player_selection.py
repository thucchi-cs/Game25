import asyncio
import pygame
from globals import *
import globals
from sprites.text import Text
import sprites.images as img

# Text variables
create_id_text = Text("fonts/COMIC.ttf", 30, "Create a Player Name", (255,255,255), 250, 200)
unique_id_text = Text("fonts/COMIC.ttf", 30, "Player Name Already Exists", (255,255,255), 250, 400)
enter_id_text = Text("fonts/COMIC.ttf", 30, "Enter Your Player Name", (255,255,255), 250, 200)
does_not_exist_text = Text("fonts/COMIC.ttf", 30, "Player Does Not Exist", (255,255,255), 250, 400)

# Player username input text box and text
input_box = pygame.Rect(70, 300, 360, 50)
username =  Text("fonts/COMIC.ttf", 30, f"", (255,255,255), 250, 325)

# Restricted text to prevent any injection risks
restricted_text = "\\/*{[]}:;?%()+=|~`<>,\"\'."
# Clock for fps
clock = pygame.time.Clock()

async def create_player(pDirt1, pDirt2):
    # Boolean variables determine what text to display
    unique_id_display = False

    # Dirt background
    dirt = pDirt1
    dirt2 = pDirt2
    background = pygame.sprite.Group()
    background.add(dirt,dirt2)

    run = True
    quit = False
    while run:
        # Timing
        clock.tick(FPS)

        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            # Update username every time a key is clicked
            elif event.type == pygame.KEYDOWN:
                # Backspace
                if event.key == pygame.K_BACKSPACE and len(username.text) >= 0:
                    username.text = username.text[:-1]
                # Check if enter is clicked and creating username
                elif event.key == pygame.K_RETURN and len(username.text) > 0:
                    # If the username entered already exists, display a wanring letting the user know
                    if username.text in globals.player_names:
                        unique_id_display = True
                    # If the username does not exist, add it to the player database and set it as the current player username
                    else:
                        globals.player_signed_in = True
                        # Initial player data
                        globals.player_data = {
                            "player_name": username.text,
                            "levels_unlocked": 1,
                            "level1_stars":[0,0,0],
                            "level2_stars":[0,0,0],
                            "level3_stars":[0,0,0]
                        }
                        # Add the data to the database
                        supabase.table("player_progress").insert(player_data).execute()
                        # Set the player username to the seleceted name
                        globals.player_username = username.text
                        run = False
                elif len(username.text) < 12 and event.unicode not in restricted_text:
                    # Add the typed letter to username text
                    username.text += event.unicode
        SCREEN.fill((0,0,0))

        # Infinite background
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
        background.draw(SCREEN)

        # Display creating username screen
        create_id_text.blit_text(SCREEN)
        pygame.draw.rect(SCREEN, (200, 200, 200), input_box, 2)
        username.blit_text(SCREEN)
        
        # Display unique ID warning if necessary
        if unique_id_display:
            unique_id_text.blit_text(SCREEN)

        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    return "quit" if quit else "continue"


async def enter_player(pDirt1, pDirt2):
    # Boolean variables determine what text to display
    does_not_exist_display = False

    # Dirt background
    dirt = pDirt1
    dirt2 = pDirt2
    background = pygame.sprite.Group()
    background.add(dirt,dirt2)

    run = True
    quit = False
    while run:
        # Timing
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
            # Update username every time a key is clicked
            elif event.type == pygame.KEYDOWN:
                # Backspacef
                if event.key == pygame.K_BACKSPACE and len(username.text) >= 0:
                    username.text = username.text[:-1]
                # Check if enter is clicked and entering username
                elif event.key == pygame.K_RETURN and len(username.text) > 0:
                    # If the username entered does not exist, display a wanrning letting the user know
                    if username.text not in globals.player_names:
                        does_not_exist_display = True
                    # If the username does exist, set it as the current player
                    else:
                        globals.player_signed_in = True
                        # Set player_data dictionary to player data from database
                        player_data_query = supabase.table("player_progress").select("*").eq("player_name", "Test2").execute()
                        globals.player_data = player_data_query.data[0]
                        globals.player_username = username.text
                        run = False
                elif len(username.text) < 12 and event.unicode not in restricted_text:
                    username.text += event.unicode
        SCREEN.fill((0,0,0))

        # Infinite background
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
        background.draw(SCREEN)

        # Display entering username screen
        enter_id_text.blit_text(SCREEN)
        pygame.draw.rect(SCREEN, (200, 200, 200), input_box, 2)
        username.blit_text(SCREEN)

        # Display non-existing player warning if necessary
        if does_not_exist_display:
            does_not_exist_text.blit_text(SCREEN)

        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    return "quit" if quit else "continue"