import pygame
import sprites.curve as curve
import globals
import numpy as np




cx = 250
cy = 300

center = (cx, cy)

test_points = [center, (cx+15,cy+25), (cx-45,cy), (cx-15,cy-25)]
test_points2 = [(cx-15,cy-25), (cx+10,cy-35), (cx+25,cy-20), (cx+27,cy+5)]
test_points3 = [(cx+27, cy+5),(cx+30,cy+40), (cx-35,cy+60), (cx-45, cy+5)]

test_curve = np.array(curve.draw_Bezier(test_points))
test_curve2 = np.array(curve.draw_Bezier(test_points2))
test_curve3 = np.array(curve.draw_Bezier(test_points3))

final_test_path = np.vstack((test_curve, test_curve2, test_curve3))

# print("1: ", test_curve)
# print("2: ", test_curve2)
# print("Final: ", final_test_path)

run = True
while run:
    for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
    
    globals.SCREEN.fill((0,0,0))


    pygame.draw.lines(globals.SCREEN, (0,0,255), False, final_test_path)
    # pygame.draw.lines(globals.SCREEN, (0,0,255), False, test_curve2)

    # for point in test_points:
    #     pygame.draw.circle(globals.SCREEN, (0,255,0), point, 5)
    # for point in test_points2:
    #     pygame.draw.circle(globals.SCREEN, (255,0,0), point, 5)
    pygame.display.flip()

