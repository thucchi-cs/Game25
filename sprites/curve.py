        
def draw_Bezier(points, speed=1):
    t = 0
    path = []
    while t <= 1:
        x = [i[0] for i in points]
        y = [i[1] for i in points]
        posX = calc_Bezier(x, t, 1, len(x)-1)
        posY = calc_Bezier(y, t, 1, len(y)-1)
        # pygame.draw.circle(screen, (255,255,255), (posX, posY), 2.5)
        path.append((posX, posY))
        t += 0.05 * speed
    return path

def calc_Bezier(circles_group, t, k, count):
    power = len(circles_group)-1 - count
    if count <= 0:
        return ((1-t)**power)*circles_group[0]
    else:
        return calc_Bezier(circles_group, t, len(circles_group) -1 , count-1) + ((k*(1-t)**power)*(t**count)*circles_group[count])

