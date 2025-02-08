# import pygame
import json
from constants import *
import sprites.text as text
import pygame
import sprites.window as window

# Move all players
def move_players(key):
    for fly in players:
        fly.move_arrows(key, pygame.sprite.Group(walls, gates, rocks, waters, elevators, buttons, frogs))
        fly.elevator_move(elevators)
        fly.check_web(webs)
        fly.check_btn(buttons)

        if fly.stuck:
            other_flies = [i for i in players if i != fly]
            fly.save_friend(other_flies)

        # Check if player reached the end
        if fly.check_end(ends):
            fly.move_off_screen()
                # players.remove(fly)
                # all.remove(fly)

def set_up_end():
    for fly in players:
        fly.end = True
        fly.current_image = fly.story_paths[0]
        fly.size = (50, 70)

def check_win():
    for fly in players:
        if not fly.hide:
            return False
    return True

# Auto scroll
def auto_scroll(counter,d1,d2):
    if counter % SPEEDFACTOR == 0:
        addition = 0
        fly_pos = 0
        for fly in players:
            if fly.rect.y > HEIGHT // 3:
                break
            fly_pos += fly.rect.y
        else:
            fly_pos /= len(players)
            addition = int((HEIGHT - fly_pos) / HEIGHT * 3)

        for sprite in pygame.sprite.Group(all, preload, d1, d2):
            sprite.scroll(addition)

        if d1.rect.y>1200:
            d1.rect.y=d2.rect.y - 1200
        if d2.rect.y >1200:
            d2.rect.y=d1.rect.y-1200
        return True
    return False

# Load the level layout from json file
def load_layout(filename):
    global smth
    # Open and load file
    file = open('levels/layouts/' + filename, 'r')
    data = json.load(file)

    # Create each object in json file
    for obj,args in data.items():
        i = -1
        while not obj[:i].isalpha():
            i -= 1
        object = obj[:i]
        # Arguments to be passed in when making the object
        arguments = []

        # Iterate through the arguments
        for v in args.values():
            # Convert to tuple if necessary
            if (type(v) == str) and (('(' in v) and (')' in v)):
                v = v[1:-1]
                v = v.split(',')
                v = (float(v[0]), float(v[1]))
            # Add arguments to list
            arguments.append(v)
        
        # Assign sprite to button
        if object == 'btn':
            sprite = preload.sprites()[-1]
            arguments.append(sprite)
        
        
        # Create object and add to groups
        # print(obj)
        temp = OBJECTS[object](*arguments)
        GROUPS[object].add(temp)
        preload.add(temp)

        
def load_on_screen():
    # pass
    for obj in preload.sprites()[:]:
        if obj.rect.bottom > 0:
            all.add(obj)
            preload.remove(obj)
    
    for obj in all.sprites()[:]:
        if obj.rect.top > HEIGHT + 20:
            obj.kill()


def fade_out(fade_level):
    alpha = fade_level + FADE_FACTOR
    if alpha > 100:
        return 100
    FADE_SURFACE.fill((0,0,0, alpha))
    SCREEN.blit(FADE_SURFACE, (0,0))
    return alpha

def fade_in(fade_level):
    alpha = fade_level - FADE_FACTOR
    if alpha < 0:
        return 0
    FADE_SURFACE.fill((0,0,0, alpha))
    SCREEN.blit(FADE_SURFACE, (0,0))
    return alpha

def fade_out_animation(clock):
    fade = 0
    while fade < 100:
        clock.tick(FPS)
        fade = fade_out(fade)
        pygame.display.flip()

def fade_in_animation(fade):
    if fade > 0:
            fade = fade_in(fade)
    pygame.display.flip()
    return fade

def reset_sprites():
    for obj in all.sprites()[:]:
        if type(obj) != flies.Flies:
            all.remove(obj)
            obj.kill()
        else:
            obj.reset()
    for obj in preload.sprites()[:]:
        preload.remove(obj)
        obj.kill()
    
    # Reset the player list
    for player in players:
        player.reset()

def restart_transition(clock):
    restart_window = window.Window("graphics/restart.png")
    clicked = False
    zoomIn = True
    while not clicked:
        clock.tick(FPS)
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        if zoomIn:
            zoomIn = restart_window.zoomIn()
        
        restart_window.draw()
        pygame.display.flip()
        