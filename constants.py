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
import sprites.obstacles.webs as web
import sprites.text as text
import sprites.obstacles.end as end


# Set up screen
WIDTH = 500
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSA Game 2025")

pygame.font.init()

# Frames timing
FPS = 40    

# Autoscrolling speed
SPEED = 1
SPEEDFACTOR = 5

# Control keys
ARROWS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
WASD = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
TFGH = [pygame.K_t, pygame.K_g, pygame.K_f, pygame.K_h]
IJKL = [pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l]

# Sprites
fly1 = flies.Flies(275, 500, ARROWS)
fly2 = flies.Flies(225, 500, WASD)
fly3 = flies.Flies(175, 500, TFGH)
fly4 = flies.Flies(325, 500, IJKL)

# Text for web
save_text = text.Text("freesansbold.ttf", 30, "Test", (83,83,140), 250, 50)

# Sprite Groups
playercount = 4
players = pygame.sprite.Group()
players.add(fly1, fly2,fly3,fly4)
buttons = pygame.sprite.Group()
webs = pygame.sprite.Group()
gates = pygame.sprite.Group()
rocks = pygame.sprite.Group()
exclamations = pygame.sprite.Group()
waters = pygame.sprite.Group()
lasers = pygame.sprite.Group()
elevators = pygame.sprite.Group()
walls = pygame.sprite.Group()
ends = pygame.sprite.Group()
all = pygame.sprite.Group(players)

# Sprites and groups dicts for json planning
OBJECTS = {'btn': button.Buttons, 'wall': wall.Wall, 
            'elevator': elevator.Elevators, 'gate': gate.Gate,
            'laser': laser.Lasers, 'rock': rock.Rocks,
            'water': water.Water, 'web': web.Web, 'end': end.End}

GROUPS = {'btn': buttons, 'wall': walls, 
            'elevator': elevators, 'gate': gates,
            'laser': lasers, 'rock': rocks,
            'water': waters, 'web': webs, 'end': ends}