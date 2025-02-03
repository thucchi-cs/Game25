# import pygame
import json
from constants import *
import sprites.text as text

# Move all players
def move_players(key):
    for fly in players:
        fly.move_arrows(key, pygame.sprite.Group(walls, gates, rocks, waters, elevators, buttons, lasers, frogs))
        fly.elevator_move(elevators)
        fly.check_web(webs)
        fly.check_btn(buttons)

        fly.check_web(webs)
        if fly.stuck:
            other_flies = [i for i in players if i != fly]
            fly.save_friend(other_flies)

        # Check if player reached the end
        if fly.check_end(ends):
                players.remove(fly)
                all.remove(fly)


# Auto scroll
def auto_scroll(counter):
    if counter % SPEEDFACTOR == 0:

        for sprite in pygame.sprite.Group(all, preload):
            sprite.scroll()
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
        temp = OBJECTS[object](*arguments)
        GROUPS[object].add(temp)
        preload.add(temp)

        
def load_on_screen():
    for obj in preload.sprites()[:]:
        if obj.rect.bottom > 0:
            all.add(obj)
            preload.remove(obj)
    
    for obj in all.sprites()[:]:
        if obj.rect.top > HEIGHT + 20:
            obj.kill()


        
        
        