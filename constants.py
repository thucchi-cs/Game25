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


# Set up screen
WIDTH = 500
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSA Game 2025")

# Frames timing
FPS = 40    

# Autoscrolling speed
SPEED = 1
SPEEDFACTOR = 2

# Control keys
ARROWS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
WASD = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
TFGH = [pygame.K_t, pygame.K_g, pygame.K_f, pygame.K_h]
IJKL = [pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l]

OBJECTS = {'btn': button.Buttons, 'wall': wall.Wall, 
            'elevator': elevator.Elevators, 'gate': gate.Gate,
            'laser': laser.Lasers, 'rock': rock.Rocks,
            'water': water.Water, 'web': web.Web}

# Sprites
fly1 = flies.Flies(250, 300, ARROWS)
fly2 = flies.Flies(250, 300, WASD)
fly3 = flies.Flies(250, 300, TFGH)
fly4 = flies.Flies(250, 300, IJKL)

wall1 = wall.Wall((100, 50), (300, 100))
web1 = web.Web(50, (100, 200))
gate1 = gate.Gate(50, (200,200), 1)
rock1 = rock.Rocks((100,100),(100,-3000),20)
water1 = water.Water((100,200),(100,100))
laser1 = laser.Lasers(250, 400, 1, (200, 5), 0)
laser2 = laser.Lasers(250, 100, 2, (500, 10), 45)
laser3 = laser.Lasers(100, 300, 3, (250, 15), 122)
elevator1 = elevator.Elevators(100, 100, (100, 200), True, 300)
elevator2 = elevator.Elevators(400, 300, (50, 100), False, 100)
button1 = OBJECTS['btn'](250, 500, water1)

# Sprite Groups
players = pygame.sprite.Group()
players.add(fly1, fly2, fly3, fly4)
buttons = pygame.sprite.Group()
buttons.add(button1)
webs = pygame.sprite.Group()
webs.add(web1)
gates = pygame.sprite.Group()
gates.add(gate1)
rocks = pygame.sprite.Group()
rocks.add(rock1)
exclamations = pygame.sprite.Group()
exclamations.add(rock1.exclamation)
waters = pygame.sprite.Group()
waters.add(water1)
lasers = pygame.sprite.Group()
lasers.add(laser1, laser2, laser3)
elevators = pygame.sprite.Group()
elevators.add(elevator1, elevator2)
walls = pygame.sprite.Group()
walls.add(wall1, elevators)
all = pygame.sprite.Group()
all.add(buttons, rocks, exclamations, waters, lasers, elevators, walls, webs, players, gates)