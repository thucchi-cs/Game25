# Libraries imports
import asyncio
import pygame
from constants import *
# import constants
import levels.helpers as h
import threading
import sprites.window as window

# Level 3 loop
async def restart():
    clock = pygame.time.Clock()
    restart_window = window.Window("graphics/restart.png")
    clicked = False
    zoomIn = True
    while not clicked:
        # print("hi")
        clock.tick(FPS)
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                clicked = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        if zoomIn:
            zoomIn = restart_window.zoomIn()
        
        restart_window.draw()
        pygame.display.flip()
         
        await asyncio.sleep(0)
    
    h.fade_out_animation(clock)
    
    return "restart"
        