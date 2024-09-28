# Imports
import pygame
import sprites.flies as flies
import sprites.wall as wall

# Set up screen
WIDTH = 1000
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSA Game 2025")

# Frames timing
FPS = 40    

# Sprites
fly = flies.Flies(500, 300)
wall1 = wall.Wall((100, 50), (300, 100), 2)
wall2 = wall.Wall((400,50),(500,100),2)
wall3 = wall.Wall((600,400),(700,500),2)

# Sprite Groups
people = pygame.sprite.Group()
people.add(fly)
walls = pygame.sprite.Group()
walls.add(wall1,wall2,wall3)