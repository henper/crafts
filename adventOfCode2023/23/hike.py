from example import trails
from itertools import permutations, pairwise
import pygame

rows = len(trails)
cols = len(trails[0])

start = (1, 0)
goal  = (cols-2, rows-1, 0)

# figure out the canvas
S = SCALING = 25
HEIGHT = rows * S
WIDTH  = cols * S

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
level = pygame.Surface((WIDTH, HEIGHT))

for y in range(rows):
    for x in range(cols):
        if trails[y][x] == '#':
            woods = pygame.Rect(x*S, y*S, S, S)
            pygame.draw.rect(level, pygame.Color('chartreuse4'), woods)
level = level.convert()

screen.blit(level, (0,0))
pygame.display.flip()

hiker_colors = [
    pygame.Color('firebrick1'),
    pygame.Color('firebrick2'),
    pygame.Color('firebrick3'),
    pygame.Color('firebrick4'),
    pygame.Color('black')
]

clock = pygame.time.Clock()
def event_loop(nobreak = False):
    while True:
        event = pygame.event.poll() # get event immediately, if any
        # Allow for ways to exit the application
        if event.type == pygame.QUIT: # closing the (proverbial) window
            pygame.quit(); exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
            pygame.quit(); exit()

        if not nobreak and event.type == pygame.MOUSEBUTTONDOWN:
            break

        clock.tick(60)

def visrep(paths, dead):
    for path in paths:
        if len(path) >= len(hiker_colors):
            for i in range(1,len(hiker_colors)+1):
                x, y, _ = path[-i]
                hiker = pygame.Rect(x*S, y*S, S, S)
                pygame.draw.rect(screen, hiker_colors[i-1], hiker)


    for path in dead:
        x, y, _ = path[-1]
        hiker = pygame.Rect(x*S, y*S, S, S)
        pygame.draw.rect(screen, pygame.Color('firebrick4'), hiker)
    pygame.display.flip()
    event_loop()

from numpy import array
north = array(( 0,-1))
south = array(( 0, 1))
east  = array(( 1, 0))
west  = array((-1, 0))

# filter functions
def inside(pos):
    x, y = pos
    return y >= 0 and y < rows and x >= 0 and x < cols

def passable(dir):
    x,y = dir
    t = trails[y][x]
    return t != '#'

def directions(pos):
    n = tuple(north + array(pos))
    s = tuple(south + array(pos))
    e = tuple(east  + array(pos))
    w = tuple(west  + array(pos))

    return [n, e, w, s]

    # if we're on an icy slope, there is no way up (well, down since we're backtracking)
    x,y = pos
    t = trails[y][x]
    if t == 'v':
        return [n]
    if t == '<':
        return [e]
    if t == '>':
        return [w]
    if t == '^':
        return [s]
    return [n, e, w, s]

def mapper(paths: list, dead: list):
    new = False
    fro = []


    for path in paths: # note, shallow copy
        x,y,c = path[-1]
        dirs = directions((x,y))

        # dont go out of bounds
        dirs = list(filter(lambda dir: inside(dir), dirs))

        # dont backtrack
        step = [(x,y) for x,y,_ in path]
        dirs = list(filter(lambda dir: dir not in step, dirs))

        # dont venture off into the woods
        dirs = list(filter(lambda dir: passable(dir), dirs))

        if not dirs:
            dead.append(path) # this is where the journey ends, we wil keep stepping in place until all journeys end
            continue

        new = True # we've taken a step in one or more directions

        # at this point we need to clone ourselves and continue in more than one direction
        for i in range(1, len(dirs)):
            x,y = dirs[i]
            clone = path.copy()
            clone.append((x, y, c + 1))
            fro.append(clone)

        # if we're merely continuing on the path, then add this one step
        if len(dirs) >= 1:
            x,y = dirs[0]
            path.append((x, y, c + 1))
            fro.append(path)



    return new, fro, dead


def pretty_print(paths, dead):
    map = [list(row) for row in trails]

    for path in paths:
        x, y, _ = path[-1]
        map[y][x] = 'O'

    for path in dead:
        x, y, _ = path[-1]
        map[y][x] = 'X'

    for row in map:
        print(" ".join(row))

    print('')

# start from the end
paths = [[goal]]

# each mapper fills in the squares directly reachable from the current squares not yet mapped
new, paths, dead = mapper(paths, [])

visrep(paths, dead)
while(new): # stop when we can't reach any more squares
    new, paths, dead = mapper(paths, dead)
    visrep(paths, dead)

    continue

    # Run ahead and kill off hikers when any one detects the footprints of another
    for pairs in permutations(paths, 2):
        killer, victim = pairs

        last_steps = [(x,y) for x,y,_ in killer[-2:]]
        steps = [(x,y) for x,y,_ in victim]
        for two_step in pairwise(steps):
            if list(two_step) == last_steps:

                x,y,k = killer[-1]
                _,_,v =victim[steps.index((x,y))]

                if k > v:
                    # killer finds and shoots his victim
                    paths.remove(victim)
                    dead.append(victim)
                else:
                    print('tf')


journey_lengths = []
for path in dead:
    x,y,c = path[-1]
    if (x,y) == start:
        journey_lengths.append(c)

print(journey_lengths)
print(max(journey_lengths))


# the ones that made it out without being killed or lost in the woods
def at_start(pos):
    x,y,_ = pos[-1]
    return start == (x,y)

actually_alive = list(filter(lambda path: at_start(path), dead))
life_lived = [len(hiker) for hiker in actually_alive]
print(max(life_lived))

longest_hike = actually_alive[life_lived.index(max(life_lived))]
for x,y,_ in longest_hike:
        hiker = pygame.Rect(x*S, y*S, S, S)
        pygame.draw.rect(screen, pygame.Color('gold'), hiker)

pygame.display.flip()
event_loop(True)
