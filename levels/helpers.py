# import pygame
import json
from constants import *

# Move all players
def move_players(key):
    for fly in players:
        fly.move_arrows(key, pygame.sprite.Group(walls, gates, rocks, waters, elevators, buttons))
        fly.elevator_move(elevators)
        fly.check_web(webs)
        fly.check_btn(buttons)

# Auto scroll
def auto_scroll(counter):
    if counter % SPEEDFACTOR == 0:
        for sprite in all:
            sprite.scroll()

# Load the level layout from json file
def load_layout(filename):
    # Open and load file
    file = open('levels/layouts/' + filename, 'r')
    data = json.load(file)
    
    # Create each object in json file
    for obj,args in data.items():
        object = obj[:-1]
        # Arguments to be passed in when making the object
        arguments = []

        # Create buttons
        if object == 'btn':
            # Create arguments
            pos = args['pos'][1:-1]
            pos = pos.split(',')
            pos = (int(pos[0]), int(pos[1]))
            sprite = all.sprites()[-1]
            arguments = [pos, sprite]

        # Create obstacles
        else:
            # Iterate through the arguments
            for v in args.values():
                # Convert to tuple if necessary
                if (type(v) == str) and (('(' in v) and (')' in v)):
                    v = v[1:-1]
                    v = v.split(',')
                    v = (int(v[0]), int(v[1]))
                # Add arguments to list
                arguments.append(v)

        # Create object and add to groups
        temp = OBJECTS[object](*arguments)
        GROUPS[object].add(temp)
        all.add(temp)