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

# Control keys
ARROWS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
WASD = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
TFGH = [pygame.K_t, pygame.K_g, pygame.K_f, pygame.K_h]
IJKL = [pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l]

# Sprites
fly = flies.Flies(250, 300, ARROWS)
wall1 = wall.Wall((100, 50), (300, 100), 2)
wall2 = wall.Wall((400,50),(500,100),2)
wall3 = wall.Wall((600,400),(700,500),2)
button1 = button.Buttons(250, 500)

# Sprite Groups
people = pygame.sprite.Group()
people.add(fly)
walls = pygame.sprite.Group()
walls.add(wall1,wall2,wall3)
buttons = pygame.sprite.Group()
buttons.add(button1)