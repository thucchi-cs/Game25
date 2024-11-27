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
SPEED = 0
SPEEDFACTOR = 2

# Control keys
ARROWS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
WASD = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
TFGH = [pygame.K_t, pygame.K_g, pygame.K_f, pygame.K_h]
IJKL = [pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l]

OBJECTS = {'btn': button.Buttons, 'wall': wall.Wall, 
            'elevator': elevator.Elevators, 'gate': gate.Gate,
            'laser': laser.Lasers, 'rock': rock.Rocks,
            'water': water.Water, 'web': web.Web, 'end': end.End}

# Sprites
fly1 = flies.Flies(250, 300, ARROWS)
fly2 = flies.Flies(250, 300, WASD)
fly3 = flies.Flies(250, 300, TFGH)
fly4 = flies.Flies(250, 300, IJKL)

txt = text.Text("fonts/wingding.ttf", 12, "My name is Ronin Gambill", "red", 100, 100)

web1 = web.Web(25, (100, 100))


save_text = text.Text("freesansbold.ttf", 25, "Test", (0,255,0), 250, 300)
# Sprite Groups
playercount = 4
players = pygame.sprite.Group()
players.add(fly1, fly2,fly3,fly4)
buttons = pygame.sprite.Group()
# buttons.add(button1)
webs = pygame.sprite.Group()
webs.add(web1)
gates = pygame.sprite.Group()
# gates.add(gate1)
rocks = pygame.sprite.Group()
# rocks.add(rock1)
exclamations = pygame.sprite.Group()
# exclamations.add(rock1.exclamation)
waters = pygame.sprite.Group()
# waters.add(water1)
lasers = pygame.sprite.Group()
# lasers.add(laser1, laser2, laser3)
elevators = pygame.sprite.Group()
# elevators.add(elevator1, elevator2)
walls = pygame.sprite.Group()
# walls.add(wall1, elevators)
ends = pygame.sprite.Group()

all = pygame.sprite.Group()
all.add(buttons, rocks, exclamations, waters, lasers, elevators, walls, webs, players, gates,ends)

GROUPS = {'btn': buttons, 'wall': walls, 
            'elevator': elevators, 'gate': gates,
            'laser': lasers, 'rock': rocks,
            'water': waters, 'web': webs, 'end': ends}