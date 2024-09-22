# Libraries import
import asyncio
import pygame

# Files imports
import sprites.person as person
import levels.level1 as level1
import sprites.wall as wall

# Set up screen
WIDTH = 1000
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSA Game 2025")

# Frames timing
clock = pygame.time.Clock()
FPS = 40

# Music
pygame.mixer.init()
pygame.mixer.music.load('music/GARREG.mp3')
pygame.mixer.music.play(-1)


# Game
async def main():
    # Sprites
    people = pygame.sprite.Group()
    guy = person.Person('guy.png', 0, 0)
    girl = person.Person('girl.png', 0, 0)
    small1 = person.Person('guy.png', 0, 0)
    small2 = person.Person('girl.png', 0, 0)
    fly = person.Person('fly.png', 500, 300)
    people.add(guy, girl, small1, small2, fly)

    walls = pygame.sprite.Group()
    wall1 = wall.Wall((100, 50), (300, 100))
    walls.add(wall1)

    # Run level 1
    await level1.level(people, guy, girl, small1, small2, fly, walls, wall1, SCREEN)


asyncio.run(main())