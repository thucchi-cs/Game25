# import pygame, random
# from tinydb import TinyDB, Query
# from constants import *

# # player_database = TinyDB('player_data.json')
# Player = Query()

# player_database.truncate()
# player_database.insert({'username':"", 'level1':{'unlocked':True, 'completed':False, 'star1':False, 'star2':False, 'star3':False}, 'level2':{'unlocked':False, 'completed':False, 'star1':False, 'star2':False, 'star3':False}, 'level3':{'unlocked':False, 'completed':False, 'star1':False, 'star2':False, 'star3':False}})

# # player = player_database.get(Player.username == "")
# # player["level2"]["unlocked"] = True

# # player_database.update(player, Player.username == "")
# run = True
# while run:
#     control = input("Add, Print or Quit: ")
    
#     if control == "a":
#         player_id = input("Enter your player ID: ")
#         if player_database.contains(Player.username == player_id):
#             print("Player ID already exists")
#         else:
#             print("Player added")
#             player_database.insert({'username':player_id, 'level1':{'unlocked':True, 'star1':False, 'star2':False, 'star3':False}, 'level2':{'unlocked':False, 'star1':False, 'star2':False, 'star3':False}})
    
#     if control == 'p':
#         print(player_database.all())
    
#     if control == 'q':
#         run = False


from supabase import create_client, Client

SUPABASE_URL = "https://mdkntldyibqyhdxddupt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1ka250bGR5aWJxeWhkeGRkdXB0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk5MTI2ODksImV4cCI6MjA1NTQ4ODY4OX0.-NDON99SnurriDTnjGRimxgOnhDXYRKE2spKknTsfxM"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

player_data = {
    "levels_unlocked": 1,
    "level1_stars":[0,0,0],
    "level2_stars":[0,0,0],
    "level3_stars":[0,0,0]
}

supabase.table("player_progress").update(player_data).eq("player_name", "Test").execute()



# response = supabase.table("player_progress").select("*").eq("player_name", "Test2").execute()
# print(response.data[0])


# response = supabase.table("player_progress").select("levels_unlocked").eq("player_name", "Test2").execute()
# levels_unlocked = response.data[0]["levels_unlocked"]

# print(levels_unlocked)



# response = supabase.table("player_progress").update({
#     "level2_stars": [1, 0, 1]  # Replacing the entire JSON array
# }).eq("player_name", "Test").execute()

# print(response)



# # response = supabase.table("player_progress").select("player_name").execute()
# # player_names = [row["player_name"] for row in response.data]


# supabase.table("player_progress").insert(player_data).execute()

# print(response)
