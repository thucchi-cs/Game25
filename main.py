# Libraries import
import asyncio
import pygame

# Files imports
import sprites.person as person
import levels.level1 as level1

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
    guy = person.Person('guy.png', 200, 100)
    girl = person.Person('girl.png', 600, 100)
    people.add(guy, girl)

    # Run level 1
    await level1.level(people, guy, girl, SCREEN)


asyncio.run(main())