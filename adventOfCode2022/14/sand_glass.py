import pygame
from time import sleep

SCALING = 4

scan_lines = []
with open('./adventOfCode2022/14/input.txt', 'r') as cave:
    for rock in cave:

        # list comprehension inception for enhanced legibility
        line = [(int(x),int(y)) for x,y in [c.split(',') for c in rock.split()[::2]]]
        scan_lines.append(line)

sand = []
rocks = []

for rock in scan_lines:
    for point in range(1, len(rock)):
        rocks.append((rock[point-1], rock[point])) # save line segment

floor = max([max(rock, key=lambda y:y[1]) for rock in rocks], key=lambda y:y[1])[1] + 2

right = max([max(rock, key=lambda x:x[0]) for rock in rocks], key=lambda x:x[0])[0]
left  = min([min(rock, key=lambda x:x[0]) for rock in rocks], key=lambda x:x[0])[0]
width = (right - left) + 400
width += width % 2 #make even for offset

OFFSET = int(width/2) + 1

def scale(p):
    x,y=p
    x = ((x - 500) + OFFSET) * SCALING
    y = y * SCALING
    return (x,y)

scaled_rocks = []
for rock in rocks:
    p1, p2 = rock
    scaled_rocks.append((scale(p1), scale(p2)))
rocks = scaled_rocks

# floor
rocks.append(((0, floor*SCALING), (width*SCALING, floor*SCALING)))

HEIGHT = floor * SCALING
screen = pygame.display.set_mode((width * SCALING, (1+floor) * SCALING))
static = screen.copy()

ROCK = (255, 255, 255)
SAND = (210, 170, 110)
BACK = (  0,   0,   0)

def collides(grain : pygame.Rect):
    for rock in rocks:
        if grain.clipline(rock):
            return True

    if (grain.collidelist(sand)) != -1:
        return True

    return False

# fill in static background
for rock in rocks:
    pygame.draw.line(static, ROCK, rock[0], rock[1], width=SCALING)

screen.blit(static, (0,0))
pygame.display.flip()
#screen.fill(BACK)

abyss = False
blocked = False
while not abyss and not blocked:

    # create hitbox for the new grain of sand
    x,y = (OFFSET * SCALING, 0)
    grain = pygame.Rect(0,0,SCALING,SCALING)
    grain.center = (x,y)

    # blocked?
    if collides(grain):
        blocked = True

    while not blocked:

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

        if grain.center[1] > floor * SCALING:
            abyss = True
            break

        grain = grain.move((dx*SCALING, dy*SCALING))

        """ animate flowing sand
        screen.blit(static, (0,0))
        pygame.draw.circle(screen, SAND, grain.center, SCALING/2)
        pygame.display.flip()
        screen.fill(BACK) """


    # add the stationary grain of sand to static background
    pygame.draw.circle(screen, SAND, grain.center, SCALING/2)
    if len(sand) % 100:
        pygame.display.flip()

print(len(sand))

while True:
    event = pygame.event.wait() # sleep until the user acts
    # Allow for ways to exit the application
    if event.type == pygame.QUIT: # closing the (proverbial) window
        break
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        break

pygame.quit()
