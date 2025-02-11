import asyncio
from constants import *
from sprites.text import Text
import sprites.menuButtons as btn

# Text variables
first_time_text = Text("fonts/COMIC.ttf", 30, f"Is this your first time playing?", (255,255,255), 250, 200)
create_id_text = Text("fonts/COMIC.ttf", 30, f"Create a player ID", (255,255,255), 250, 200)
enter_id_text = Text("fonts/COMIC.ttf", 30, f"Enter your player ID", (255,255,255), 250, 200)


# Buttons
yes_btn = btn.menuBtn((50, 50), (WIDTH // 2 + 50, HEIGHT // 2 + 50), 'yes_button.png')
no_btn = btn.menuBtn((50, 50), (WIDTH // 2 - 50, HEIGHT // 2 + 50), 'no_button.png')
buttons = pygame.sprite.Group()
buttons.add(yes_btn, no_btn)

# Player ID input text box and text
input_box = pygame.Rect(100, 300, 300, 50)
player_id =  Text("fonts/COMIC.ttf", 30, f"", (255,255,255), 250, 325)

# Valid input restricts player id to only letters and numbers
def valid_id(id):
    valid_input = ['abcdefghijklmnopqrstuvwxyz0123456789']
    for letter in id:
        if letter not in valid_input:
            return False
    return True

async def select_player():
    show_question = True
    show_yes = False
    show_no = False
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
                # If click yes
                if yes_btn.is_clicked():
                    show_yes = True
                    show_question = False
                # If click no
                if no_btn.is_clicked():
                    show_no = True
                    show_question = False
            elif event.type == pygame.KEYDOWN and (show_yes or show_no):
                if event.key == pygame.K_BACKSPACE and len(player_id.text) > 0:
                    player_id.text = player_id.text[:-1]
                elif event.key == pygame.K_RETURN and len(player_id.text) > 0:
                    pass
                else:
                    player_id.text += event.unicode
        SCREEN.fill((0,0,0))

        if show_question:
            first_time_text.blit_text(SCREEN)
            buttons.draw(SCREEN)
        elif show_yes:
            create_id_text.blit_text(SCREEN)
            pygame.draw.rect(SCREEN, (200, 200, 200), input_box, 2)
            player_id.blit_text(SCREEN)
        elif show_no:
            enter_id_text.blit_text(SCREEN)
            pygame.draw.rect(SCREEN, (200, 200, 200), input_box, 2)
            player_id.blit_text(SCREEN)


        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    return "quit" if quit else "continue"
