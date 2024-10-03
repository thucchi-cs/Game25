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

# Sprites
fly = flies.Flies(250, 300)
wall1 = wall.Wall((100, 50), (300, 100), 2)
wall2 = wall.Wall((400,50),(500,100),2)
wall3 = wall.Wall((600,400),(700,500),2)
button1 = button.Buttons(250, 500)
web1 = web.Web(50, (100, 200))
gate1 = gate.Gate(50, (200,200), 1)

# Sprite Groups
players = pygame.sprite.Group()
players.add(fly)
walls = pygame.sprite.Group()
walls.add(wall1,wall2,wall3)
buttons = pygame.sprite.Group()
buttons.add(button1)
webs = pygame.sprite.Group()
webs.add(web1)
gates = pygame.sprite.Group()
gates.add(gate1)