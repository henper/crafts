import pygame
import numpy as np

maze = [
    '###############',
    '#.......#....E#',
    '#.#.###.#.###.#',
    '#.....#.#...#.#',
    '#.###.#####.#.#',
    '#.#.#.......#.#',
    '#.#.#####.###.#',
    '#...........#.#',
    '###.#.#####.#.#',
    '#...#.....#.#.#',
    '#.#.#.###.#.#.#',
    '#.....#...#.#.#',
    '#.###.#.#.#.#.#',
    '#S..#.....#...#',
    '###############',
]

maze = [
    '#################',
    '#...#...#...#..E#',
    '#.#.#.#.#.#.#.#.#',
    '#.#.#.#...#...#.#',
    '#.#.#.#.###.#.#.#',
    '#...#.#.#.....#.#',
    '#.#.#.#.#.#####.#',
    '#.#...#.#.#.....#',
    '#.#.#####.#.###.#',
    '#.#.#.......#...#',
    '#.#.###.#####.###',
    '#.#.#...#.....#.#',
    '#.#.#.#####.###.#',
    '#.#.#.........#.#',
    '#.#.#.#########.#',
    '#S#.............#',
    '#################',
]

#from input import maze

def passable(to):
    y,x = to
    return maze[y][x] != '#'

def cheaper(to, c):
    global scan
    global visited

    try:
        i = visited.index(to)
        prev_c = scan[i][2]
        return prev_c > c
    except ValueError:
        return True

    return True

def directions(pos):
    north = tuple(np.array((-1, 0)) + np.array(pos))
    south = tuple(np.array(( 1, 0)) + np.array(pos))
    east  = tuple(np.array(( 0, 1)) + np.array(pos))
    west  = tuple(np.array(( 0,-1)) + np.array(pos))
    return [north, south, east, west]

def mapper(squares):
    new = []
    for square in squares:
        pos,dir,c = square

        if pos == end:
            costs.append(c)
            continue

        steps = directions(pos)

        # dont backtrack
        prev_pos = np.array(pos) - np.array(dir)
        steps = list(filter(lambda step: not np.array_equal(step, prev_pos), steps))

        # follow maze
        steps = list(filter(lambda step: passable(step), steps))

        # don't tread on cheaper paths
        #steps = list(filter(lambda step: cheaper(step, c), steps))

        #path = [p for p,_,_ in scan]
        #steps = list(filter(lambda step: step not in path, steps))

        for step in steps:
            nc = c + 1

            ndir = tuple(np.array(step) - np.array(pos))
            if ndir != dir:
                nc += 1000

            new.append((step, ndir, nc))

    return list(set(new))



width  = len(maze[0])
height = len(maze)

start = (height-2, 1)
end   = (1, width-2)

costs = []
visited = []

# Visualization
SCALE = S = 8
pygame.init()
screen = pygame.display.set_mode((width*SCALE,height*SCALE))
screen.fill("black")
clock  = pygame.time.Clock()

for y in range(height):
    for x in range(width):
        if maze[y][x] == '#':
            pygame.draw.rect(screen, "green", pygame.Rect(x*S, y*S, S, S))
pygame.display.flip()

def viz_steps(steps):
    for step in steps:
        pos,_,_ = step
        pygame.draw.rect(screen, "red", pygame.Rect(pos[1]*S, pos[0]*S, S, S))
    pygame.display.flip()

scan = [((start[0], start[1]), (0,1), 0)]

new = mapper(scan)
viz_steps(new)
while(new):
    scan += new
    new = mapper(new)

    viz_steps(new)

    visited += [p for p,_,_ in new]

    print(len(new))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

print(min(costs))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    clock.tick(60)

# 17036 too low