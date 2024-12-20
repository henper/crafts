import pygame
import numpy as np

maze = [
    '#################',
    '#################',
    '##...#...#.....##',
    '##.#.#.#.#.###.##',
    '##S#...#.#.#...##',
    '########.#.#.####',
    '########.#.#...##',
    '########.#.###.##',
    '####..E#...#...##',
    '####.#######.####',
    '##...###...#...##',
    '##.#####.#.###.##',
    '##.#...#.#.#...##',
    '##.#.#.#.#.#.####',
    '##...#...#...####',
    '#################',
    '#################',
]

#from input import maze

width  = len(maze[0])
height = len(maze)

start = None
goal  = None

for y in range(height):
    for x in range(width):
        if maze[y][x] == 'S':
            start = (y,x)
        if maze[y][x] == 'E':
            goal = (y,x)

# Visualization
SCALE = S = 32
pygame.init()
screen = pygame.display.set_mode((width*SCALE,height*SCALE))
screen.fill("black")
clock  = pygame.time.Clock()
font = pygame.font.Font(None, S)

for y in range(height):
    for x in range(width):
        if maze[y][x] == '#':
            pygame.draw.rect(screen, "green", pygame.Rect(x*S, y*S, S, S))
pygame.display.flip()


def draw_cost(x,y,c, color="yellow"):
    s = str(c)
    w,h = font.size(s)
    yoffset = (S - h)/2
    xoffset = (S - w)/2

    render = font.render(s, True, color)
    screen.blit(render, (x*S + xoffset, y*S + yoffset))



# filter functions
def passable(to):
    y,x = to
    return maze[y][x] != '#'

def directions(pos, s=1):
    north = tuple(np.array((-s, 0)) + np.array(pos))
    south = tuple(np.array(( s, 0)) + np.array(pos))
    east  = tuple(np.array(( 0, s)) + np.array(pos))
    west  = tuple(np.array(( 0,-s)) + np.array(pos))
    return [north, south, east, west]

def mapper(squares):
    new = []
    for square in squares:
        y,x,c = square
        dirs = directions((y,x))

        # dont backtrack
        path = [(y,x) for y,x,_ in scan]
        dirs = list(filter(lambda dir: dir not in path, dirs))

        # dont pass thru walls
        dirs = list(filter(lambda dir: passable(dir), dirs))

        for direction in dirs:
            y, x = direction
            new.append((y, x, c + 1))

    return list(set(new))


y,x = start
scan = [(y,x,0)]

# each mapper fills in the squares directly reachable from the current squares not yet mapped
new = mapper(scan)
while(new): # stop when we can't reach any more squares
    scan += new
    new = mapper(new)


map = np.zeros((height, width), dtype=int)
for y,x,c in scan:
    map[y,x] = c
    draw_cost(x,y,c)
pygame.display.flip()


cheats = []
for y,x,c in scan:
    dirs = directions((y,x), 2)

    for dy,dx in dirs:
        shortcut = map[dy][dx]
        if shortcut != 0:

            savings = shortcut - c - 2
            if savings > 0:
                pos = np.array((y,x))
                cy,cx = pos + (np.array((dy,dx))-pos)/2

                cheats.append((cy,cx,savings))

for y,x,c in cheats:
    draw_cost(x,y,c, "red")
pygame.display.flip()

savings = np.array([c for _,_,c in cheats])
print(sum(savings >= 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    clock.tick(60)
