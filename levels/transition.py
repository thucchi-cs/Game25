import asyncio
from constants import *
import sprites.text as text

async def transition(level_num):
    global all
    for obj in all.sprites()[:]:
        if type(obj) != flies.Flies:
            all.remove(obj)
            obj.kill()
    for obj in preload.sprites()[:]:
        preload.remove(obj)
        obj.kill()
    
    quit = False
    run = True
    display_text = text.Text("freesansbold.ttf", 30, f"Level {level_num}", (83,83,140), 500, 200)
    counter = 0
    while run:
        # Event handles
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True
        
        if display_text.center_x < 10:
            run = False
        
        counter += 1
        SCREEN.fill((0, 0, 0))
        display_text.blit_text(SCREEN)
        if counter % 5 == 0:
            display_text.center_x -= 1
        
        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    
    return quit