# import pygame
import csv
from constants import *

def move_players(key, walls, gates, rocks, waters):
    for fly in players:
        fly.move_arrows(key, walls, gates, rocks, waters)


def load_layout(file):
    # read csv file into a dictionary
    file = open('levels/layouts/level1.csv')
    layout = csv.DictReader(file)
    for obj in layout:
        args = []
        if obj['thing'] == 'btn':
            pos = obj['arg1'].split()
            pos = (int(pos[0]), int(pos[1]))
            sprite = all.sprites()[-1]
            args = [pos, sprite]
        else:
            for k,v in obj.items():
                if k != 'thing' and v != None:
                    try:
                        v = int(v)
                    except:
                        if ' ' in v:
                            v = v.split()
                            v = (int(v[0]), int(v[1]))
                        else:
                            v = bool(v)

                    args.append(v)
                    print(v, type(v))

        temp = OBJECTS[obj['thing']](*args)
        all.add(temp)
