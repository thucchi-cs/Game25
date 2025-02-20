import pygame
import globals
import sprites.curve as curve
import numpy as np


class Stars(pygame.sprite.Sprite):
    def __init__(self, pos, id):
        super().__init__()
        # Image rendering
        self.image = pygame.image.load('graphics/star.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # ID represents whcih star it is (1, 2, or 3)
        self.id = id

        # Position on top of the screen (1-3 - left-right)
        self.top_pos = (150+50*self.id, 25)
        # Indicates if the star is following its path
        self.following = False
        # Center x and y used to create path
        cx, cy = pos[0], pos[1]
        # Spiral is broken up into sections made from four different curves
        path1_control_points = [(cx,cy), (cx+15,cy+25), (cx-45,cy), (cx-15,cy-25)]
        path2_control_points = [(cx-15,cy-25), (cx+10,cy-35), (cx+25,cy-20), (cx+27,cy+5)]
        path3_control_points = [(cx+27, cy+5),(cx+30,cy+40), (cx-35,cy+60), (cx-45, cy+5)]
        path1 = np.array(curve.draw_Bezier(path1_control_points, 2))
        path2 = np.array(curve.draw_Bezier(path2_control_points, 2))
        path3 = np.array(curve.draw_Bezier(path3_control_points, 2))
        path4 = curve.draw_Bezier([path3[-1], (globals.WIDTH // 2, globals.HEIGHT // 2), self.top_pos])
        # Final path is a combination of all the portions of the path
        self.path = np.vstack((path1, path2, path3, path4))
        # Current location in path
        self.path_index = 0

        # Determines if the star has been collected
        self.collected = False

    

    # Scroll with screen
    def scroll(self, addition):
        self.rect.y += globals.SPEED + addition

    # Follow path to the top of the screen
    def animate(self):
        self.path_index += 1
        self.rect.center = self.path[self.path_index]
        if self.path_index >= len(self.path)-1:
            self.add(globals.stars_collected)
            self.remove(globals.all)

    # Update star
    def update(self):
        if self.following:
            self.animate()