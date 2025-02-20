# Imports
import pygame
import sprites.flies as flies
import sprites.wall as wall
import sprites.buttons as button
import sprites.obstacles.elevators as elevator
import sprites.obstacles.gates as gate
import sprites.obstacles.lasers as laser
import sprites.obstacles.rocks as rock
import sprites.obstacles.water as water
import sprites.obstacles.frogs as frog
import sprites.obstacles.webs as web
import sprites.text as text
import sprites.obstacles.end as end
import sprites.obstacles.keys as key
import sprites.stars as star
from supabase import create_client, Client

# Database connection information
SUPABASE_URL = "https://mdkntldyibqyhdxddupt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1ka250bGR5aWJxeWhkeGRkdXB0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk5MTI2ODksImV4cCI6MjA1NTQ4ODY4OX0.-NDON99SnurriDTnjGRimxgOnhDXYRKE2spKknTsfxM"

# Database
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Keeps track of player progress thrpughout the game
# Is used to store data locally instead of constantly updating the database
player_data = {
    "levels_unlocked": 1,
    "level1_stars":[0,0,0],
    "level2_stars":[0,0,0],
    "level3_stars":[0,0,0]
}

# Used so the player database is ony updated when the player is logged in
player_signed_in = False

# All the player name in the database, used when logging in
player_names_tale = supabase.table("player_progress").select("player_name").execute()
# Player name list of disctionaries converted to a list of names
player_names = [row["player_name"] for row in player_names_tale.data]

# Player username set to empty when player isn't signed in
player_username = ""

num_of_levels = 3
# Ronin Reminders (patent pending) - 1st value in size is width. 2nd is tall

# Set up screen
WIDTH = 500
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

FADE_SURFACE = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
FADE_FACTOR = 5

pygame.display.set_caption("TSA Game 2025")

pygame.font.init()

# Frames timing
FPS = 30

# Autoscrolling speed
SPEED = 1
SPEEDFACTOR = 1

# Control keys
ARROWS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
WASD = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
TFGH = [pygame.K_t, pygame.K_g, pygame.K_f, pygame.K_h]
IJKL = [pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l]

# Sprites
fly1 = flies.Flies(275, 500, ARROWS, 1)
fly2 = flies.Flies(225, 500, WASD, 2)
fly3 = flies.Flies(175, 500, TFGH, 3)
fly4 = flies.Flies(325, 500, IJKL, 4)

# Text for web
save_text = text.Text("fonts/COMIC.TTF", 30, "Test", (255,255,255), 250, 75)

key_counter = key.KeyCounter()

# Sprite Groups
players = pygame.sprite.Group()
players.add(fly1, fly2,fly3,fly4)
buttons = pygame.sprite.Group()
webs = pygame.sprite.Group()
gates = pygame.sprite.Group()
keys = pygame.sprite.Group()
keys_collected = pygame.sprite.Group()
rocks = pygame.sprite.Group()
exclamations = pygame.sprite.Group()
waters = pygame.sprite.Group()
lasers = pygame.sprite.Group()
elevators = pygame.sprite.Group()
walls = pygame.sprite.Group()
ends = pygame.sprite.Group()
frogs = pygame.sprite.Group()
stars = pygame.sprite.Group()
stars_collected = pygame.sprite.Group()
all = pygame.sprite.Group(players)
preload = pygame.sprite.Group()

# Sprites and groups dicts for json planning
OBJECTS = {'btn': button.Buttons, 'wall': wall.Wall, 
            'elevator': elevator.Elevators, 'gate': gate.Gate, 'key': key.Key,
            'laser': laser.Lasers, 'rock': rock.Rocks,
            'water': water.Water, 'frog': frog.Frog, 'web': web.Web, 'end': end.End,
            'star': star.Stars}

GROUPS = {'btn': buttons, 'wall': walls, 
            'elevator': elevators, 'gate': gates, 'key': keys,
            'laser': lasers, 'rock': rocks,
            'water': waters, 'frog': frogs, 'web': webs, 'end': ends,
            'star':stars}


#      |   |
#      |   |

#   \         /
#     \     /
#       --- 
