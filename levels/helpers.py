# import pygame
import json
from constants import *
import sprites.text as text
import pygame
import sprites.window as window
import asyncio
import sprites.curve as curve
import random
# Move all players
pygame.mixer.init()
def move_players(fly, key, tutorial=False):
    fly.move_arrows(key, pygame.sprite.Group(walls, gates, rocks, elevators, buttons, frogs))
    fly.elevator_move(elevators)
    fly.check_web(webs)
    fly.check_btn(buttons)
    fly.collideWater(waters)
    fly.check_gates(gates)
    key_collect = fly.check_keys(keys)
    if key_collect:
        path = curve.draw_Bezier([(key_collect.rect.centerx, key_collect.rect.centery), (WIDTH//2, 0), (key_counter.rect.centerx, key_counter.rect.centery)])
        key_collect.following = True
        key_collect.set_path(path)
        all.remove(key_collect)
        all.add(key_collect)

    star_collect = fly.check_stars(stars)
    if star_collect:
        path = curve.draw_Bezier([(star_collect.rect.centerx, star_collect.rect.centery), (WIDTH//2, 0), (star_counter.rect.centerx, star_counter.rect.centery)])
        star_collect.following = True
        star_collect.set_path(path)
        all.remove(star_collect)
        all.add(star_collect)

    if fly.stuck:
        other_flies = [i for i in players if i != fly]
        fly.save_friend(other_flies,webs,tutorial)

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
        addition = 0
        for fly in players:
            if fly.rect.y < HEIGHT // 6:
                addition = int((HEIGHT - fly_pos) / HEIGHT * 3)
                fly_pos /= len(players)
                break
            fly_pos += fly.rect.y
        # else:
        #     fly_pos /= len(players)

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

async def fade_out_animation(clock):
    fade = 0
    while fade < 100:
        clock.tick(FPS)
        fade = fade_out(fade)
        pygame.display.flip()
        await asyncio.sleep(0)

def fade_in_animation(fade):
    if fade > 0:
        fade = fade_in(fade)
    # pygame.display.flip()
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
    key_counter.counter = 0
    star_counter.counter = 0

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

def onButton(type):
    if type == "pause":
        if pygame.mouse.get_pos()[0] >= 15 and pygame.mouse.get_pos()[0] <= 60 and pygame.mouse.get_pos()[1] >= 15 and pygame.mouse.get_pos()[1] <=60:
            return True
    if type == "continue":
        if pygame.mouse.get_pos()[0] >= 49 and pygame.mouse.get_pos()[0] <= 445 and pygame.mouse.get_pos()[1] >= 258 and pygame.mouse.get_pos()[1] <=359:
            return True
    if type == "restart":
        if pygame.mouse.get_pos()[0] >= 47 and pygame.mouse.get_pos()[0] <= 242 and pygame.mouse.get_pos()[1] >= 373 and pygame.mouse.get_pos()[1] <=478:
            return True
    
    if type == "main":
        if pygame.mouse.get_pos()[0] >= 248 and pygame.mouse.get_pos()[0] <= 445 and pygame.mouse.get_pos()[1] >= 373 and pygame.mouse.get_pos()[1] <=478:
            return True

    return False


def isWater():

    # screenWater = False

    # if object in all: screen water = true
    # if true and not playing, play
    # if false, stop
    screenWater = False
    for object in waters:
        
        if object in all and object.show == True:
            screenWater = True


    if screenWater == True:
        if pygame.mixer.Sound.get_num_channels(waterSound) == 0:
            pygame.mixer.Sound.set_volume(waterSound,0.2)
            pygame.mixer.Sound.play(waterSound,-1)
            # print("I am playing my wonderful water sound LOL")
    else:
        if pygame.mixer.Sound.get_num_channels(waterSound) > 0:
            pygame.mixer.Sound.stop(waterSound)
            # print("I am stopping my wonderful water sound LOL")

# def isFrog():
#     print("I AM TRYING TO SEE IF THERE ARE ANY FROGS")
#     shouldCroak = random.randint(1,90)
    
#     screenFrog = False
#     for object in frogs:
#         if frogs in all:
#             screenFrog = True
#     if screenFrog == True:
#         print("I SEE A FROG RIBBIT RIBBIT ")
#         if shouldCroak == 30:
#             if pygame.mixer.Sound.get_num_channels(frogSound) == 0:
#                 pygame.mixer.Sound.set_volume(frogSound,0.5)
#                 pygame.mixer.Sound.play(frogSound)
#                 print("I am playing my wonderful frog sound LOL")
#     else:
#         pygame.mixer.Sound.stop(frogSound)

            