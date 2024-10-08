import pygame
from constants import *

def move_players(key, walls, gates, rocks, waters):
    for fly in players:
        fly.move_arrows(key, walls, gates, rocks, waters)