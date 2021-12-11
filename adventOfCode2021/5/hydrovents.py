import pygame
import re

WIDTH, HEIGHT = (1000, 1000)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

vents = []

prog = re.compile('([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)')
f = open("adventOfCode2021/5/input.txt", 'r')

for line in f:
    result = prog.match(line)
    sc = pygame.Vector2(int(result.group(1)), int(result.group(2)))
    ec = pygame.Vector2(int(result.group(3)), int(result.group(4)))

    if sc.x == ec.x or sc.y == ec.y:

        pygame.draw.line(screen, (128,128,128), sc, ec)
        vents.append((sc, ec))

pygame.display.update()


def parallel_overlapping_lines_intersections(a1, a2, b1, b2):
    global intersections

    if a1 < b1 and a2 > b1:
        intersections += a2 - b1
    if a1 > b1 and a2 > b2:
        intersections += b2 - a1
    if a1 > b1 and a2 < b2:
        intersections += a2 - a1
    if a1 < b1 and a2 > b2:
        intersections += b2 - b1
    

parallel_overlapping_lines = 0
intersections = 0
for i in range(len(vents)):

    #screen.fill((0,0,0))
    for vent in vents:
        pygame.draw.line(screen, (128,128,128), vent[0], vent[1])

    x1, y1 = vents[i][0]
    x2, y2 = vents[i][1]

    pygame.draw.line(screen, (255,0,0), (x1,y1), (x2,y2))

    for j in range(i+1, len(vents)):

        x3, y3 = vents[j][0]
        x4, y4 = vents[j][1]

        #pygame.draw.line(screen, (255,255,255), (x3,y3), (x4,y4))
        #pygame.display.update()

        tn = ((x1-x3) * (y3-y4)) - ((y1-y3)*(x3-x4))
        td = ((x1-x2) * (y3-y4)) - ((y1-y2)*(x3-x4))

        un = ((x1-x3) * (y1-y2)) - ((y1-y3)*(x1-x2))
        ud = td

        try:
            t = tn / td
            u = un / ud
        except ZeroDivisionError:
            t = -1
            u = -1

            if len(set([x1,x2,x3,x4])) == 1:
                pygame.draw.line(screen, (0,255,0), (x3,y3), (x4,y4))
                pygame.display.update()

                parallel_overlapping_lines_intersections(min(y1, y2), max(y1,y2), min(y3, y4), max(y3,y4))

            if len(set([y1,y2,y3,y4])) == 1:
                pygame.draw.line(screen, (0,255,0), (x3,y3), (x4,y4))
                pygame.display.update()

                parallel_overlapping_lines_intersections(min(x1, x2), max(x1,x2), min(x3, x4), max(x3,x4))

                

        e = 0.01
        
        if t >= 0-e and t <= 1+e and u >= 0-e and u <= 1+e:
            Px = x1+t*(x2-x1)
            Py = y1+t*(y2-y1)
            P = pygame.Vector2(Px,Py)

            pygame.draw.circle(screen, (255,255,0), (int(P.x), int(P.y)), 1)
            #pygame.display.update()
            intersections += 1


print(intersections)
pygame.display.update()


# Game loop
while True:
    event = pygame.event.wait() # sleep until the user acts

    # Allow for ways to exit the application
    if event.type == pygame.QUIT: # closing the (proverbial) window
        break
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        break