import pygame
import csv
from constants import *

def move_players(key, walls, gates, rocks, waters):
    for fly in players:
        fly.move_arrows(key, walls, gates, rocks, waters)


def load_layout(file):
    # read csv file into a dictionary
    file = open('layouts/level1.csv')
    layout = csv.DictReader(file)
    # iterate through dictionary
    for obj in layout:
        # create object based on csv row

        # x, y, size, flipped, y2      elevators
        # size, pos, direction         gates
        # x, y, n, size, angle         lasars
        # self, size, rPos, speed      rocks
        # self, pos, size              water
        # self, size, pos              webs
        # x, y, obsticle               buttons
        # size, pos                    wall
        temp = OBJECTS[obj['thing']]()
        pass
    