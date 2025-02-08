import pygame
import levels.helpers as h
from constants import *
import asyncio



async def showInstructions():
    # Image variables
    movement_instructions = pygame.image.load("graphics/PlayerControls.png")
    how_to_play1 = pygame.image.load("graphics/HowToPlay1.png")
    how_to_play2 = pygame.image.load("graphics/HowToPlay2.png")

    # Fade Variables
    clock = pygame.time.Clock()
    fade = 255

    # Quits game when true
    quit = False

    # Show player control instruction
    showing_movement_instructions = True
    while showing_movement_instructions:
        clock.tick(FPS)
        SCREEN.blit(movement_instructions, (0,0))
        fade = h.fade_in_animation(fade)

        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                quit = True
                showing_movement_instructions = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    showing_movement_instructions = False
                    quit = True
                
                # Check to skip level
                if event.key == pygame.K_TAB:
                    showing_movement_instructions = False
                    
            # Close movement instructions
            if event.type == pygame.MOUSEBUTTONDOWN:
                showing_movement_instructions = False
        
        
        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    
    # Show how to play 1
    showing_how_to1 = True
    while showing_how_to1:
        clock.tick(FPS)
        SCREEN.blit(how_to_play1, (0,0))

        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                quit = True
                showing_how_to1 = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    showing_how_to1 = False
                    quit = True
                
                # Check to skip level
                if event.key == pygame.K_TAB:
                    showing_how_to1 = False
            # Close how_to1 instructions
            if event.type == pygame.MOUSEBUTTONDOWN:
                showing_how_to1 = False
        
        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    
    # Show how to play 2
    showing_how_to2 = True
    while showing_how_to2:
        clock.tick(FPS)
        SCREEN.blit(how_to_play2, (0,0))

        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                quit = True
                showing_how_to2 = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    showing_how_to2 = False
                    quit = True
                
                # Check to skip level
                if event.key == pygame.K_TAB:
                    showing_how_to2 = False
            # Close movement instructions
            if event.type == pygame.MOUSEBUTTONDOWN:
                showing_how_to2 = False
        
        pygame.display.flip()
        # asyncio
        await asyncio.sleep(0)
    
    h.fade_out_animation(clock)
    
    return "quit" if quit else "continue"
        
        



