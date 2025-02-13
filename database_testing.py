import pygame, random
from tinydb import TinyDB, Query
from constants import *

# player_database = TinyDB('player_data.json')
Player = Query()

player_database.truncate()
player_database.insert({'username':"", 'level1':{'unlocked':True, 'completed':False, 'star1':False, 'star2':False, 'star3':False}, 'level2':{'unlocked':False, 'completed':False, 'star1':False, 'star2':False, 'star3':False}, 'level3':{'unlocked':False, 'completed':False, 'star1':False, 'star2':False, 'star3':False}})

# player = player_database.get(Player.username == "")
# player["level2"]["unlocked"] = True

# player_database.update(player, Player.username == "")
run = True
while run:
    control = input("Add, Print or Quit: ")
    
    if control == "a":
        player_id = input("Enter your player ID: ")
        if player_database.contains(Player.username == player_id):
            print("Player ID already exists")
        else:
            print("Player added")
            player_database.insert({'username':player_id, 'level1':{'unlocked':True, 'star1':False, 'star2':False, 'star3':False}, 'level2':{'unlocked':False, 'star1':False, 'star2':False, 'star3':False}})
    
    if control == 'p':
        print(player_database.all())
    
    if control == 'q':
        run = False



            