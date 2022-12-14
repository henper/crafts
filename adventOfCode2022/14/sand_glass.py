import pygame
from time import sleep

SCALING = 10
OFFSET = 450

scan_lines = []
with open('./adventOfCode2022/14/input.txt', 'r') as cave:
    for rock in cave:
        # list comprehension inception for enhanced legibility
        line = [((int(x)-OFFSET)*SCALING,(int(y))*SCALING) for x,y in [c.split(',') for c in rock.split()[::2]]]
        scan_lines.append(line)

WIDTH, HEIGHT = 125*SCALING, 200*SCALING
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ROCK = (255, 255, 255)
SAND = (210, 170, 110)

sand = []
rocks = []

for rock in scan_lines:
        for point in range(1, len(rock)):
            rocks.append((rock[point-1], rock[point])) # save line segment

def collides(grain : pygame.Rect):
    for rock in rocks:
        if grain.clipline(rock):
            return True

    if (grain.collidelist(sand)) != -1:
        return True

    return False

for rock in scan_lines:
        for point in range(1, len(rock)):
            pygame.draw.line(screen, ROCK, rock[point-1], rock[point], width=SCALING)
pygame.display.flip()
input()

abyss = False
while not abyss:

    """
    event = pygame.event.wait() # sleep until the user acts
    # Allow for ways to exit the application
    if event.type == pygame.QUIT: # closing the (proverbial) window
        break
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        break
    """

    # draw rocks
    for rock in scan_lines:
        for point in range(1, len(rock)):
            pygame.draw.line(screen, ROCK, rock[point-1], rock[point], width=SCALING)

    # draw sand at rest
    for grain in sand:
        pygame.draw.circle(screen, SAND, grain.center, SCALING/2)

    # create hitbox for the new grain of sand
    x,y = ((500 - OFFSET) * SCALING, 0)
    grain = pygame.Rect(0,0,SCALING,SCALING)
    grain.center = (x,y)

    while True:

        # fall, if possible
        dy = 1
        dx = 0 # straight
        if collides(grain.move((dx*SCALING, dy*SCALING))):
            dx = -1 # left
            if collides(grain.move((dx*SCALING, dy*SCALING))):
                dx = 1 # right
                if collides(grain.move((dx*SCALING, dy*SCALING))):
                    dx = 0
                    dy = 0

        if grain == grain.move((dx*SCALING, dy*SCALING)):
            sand.append(grain)
            break # at rest

        pygame.draw.circle(screen, (0,0,0), grain.center, SCALING)

        grain = grain.move((dx*SCALING, dy*SCALING))

        pygame.draw.circle(screen, SAND, grain.center, SCALING)
        pygame.display.flip()

        if grain.center[1] > HEIGHT:
            abyss = True
            break

        #sleep(0.002)



print(len(sand))

while True:
    event = pygame.event.wait() # sleep until the user acts
    # Allow for ways to exit the application
    if event.type == pygame.QUIT: # closing the (proverbial) window
        break
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        break

pygame.quit()
