import pygame, random
from tinydb import TinyDB, Query
from constants import *

# player_database = TinyDB('player_data.json')
# Player = Query()

# player_database.truncate()
# player_database.insert({'id':'player0','level1':{'unlocked':True, 'star1':False, 'star2':False, 'star3':False}})

run = True
while run:
    control = input("Add, Print or Quit: ")
    
    if control == "a":
        player_id = input("Enter your player ID: ")
        if player_database.contains(Player.id == player_id):
            print("Player ID already exists")
        else:
            print("Player added")
            player_database.insert({'id':player_id,'level1':{'unlocked':True, 'star1':False, 'star2':False, 'star3':False}})
    
    if control == 'p':
        print(player_database.all())
    
    if control == 'q':
        run = False



            