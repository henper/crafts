import pygame


import numpy as np

lab = [
'....#.....',
'.........#',
'..........',
'..#.......',
'.......#..',
'..........',
'.#..^.....',
'........#.',
'#.........',
'......#...',
]

start = np.array([6, 4])

from input import lab, start

y,x = start
print(lab[y][x])

height = len(lab)
width  = len(lab[0])



turns = {
    (-1, 0): ( 0, 1),
    ( 0, 1): ( 1, 0),
    ( 1, 0): ( 0,-1),
    ( 0,-1): (-1, 0),
}

dir = np.array([-1,0])

stalking_positions = [tuple(start)]

pos = start.copy()

while True:
    # Turn on the spot until there are no obstructions
    y,x = pos + dir

    if x == -1 or x == width or y == -1 or y == height:
        break

    while lab[y][x] == '#':
        dir = np.array(turns[tuple(dir)])
        y,x = pos + dir

    pos += dir
    stalking_positions.append(tuple(pos))

print(len(set(stalking_positions)))


# Visualization
SCALE = S = 16
pygame.init()
screen = pygame.display.set_mode((width*SCALE,height*SCALE))
screen.fill("black")
clock  = pygame.time.Clock()

for y in range(height):
    for x in range(width):
        if lab[y][x] == '#':
            pygame.draw.rect(screen, "green", pygame.Rect(x*S, y*S, S, S))
pygame.display.flip()

for i, pos in enumerate(stalking_positions):
    y,x = pos
    pygame.draw.circle(screen, "purple", (x*S+S/2, y*S+S/2), S/2)

    fades = 100
    for j in range(i-fades, i):
        if j < 0:
            continue

        fade = 1 - (i-j)/fades
        c = pygame.Color("purple")
        c.r = int(c.r * fade)
        c.g = int(c.g * fade)
        c.b = int(c.b * fade)

        y,x = stalking_positions[j]
        pygame.draw.circle(screen, c, (x*S+S/2, y*S+S/2), S/2)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    clock.tick(120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    clock.tick(60)
