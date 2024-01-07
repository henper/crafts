from input import garden

import pygame

rows = len(garden)
cols = len(garden[0])

# figure out the canvas
S = SCALING = 5
HEIGHT = rows * S
WIDTH  = cols * S

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
level = pygame.Surface((WIDTH, HEIGHT))

for y in range(rows):
    for x in range(cols):
        if garden[y][x] == '#':
            woods = pygame.Rect(x*S, y*S, S, S)
            pygame.draw.rect(level, pygame.Color('chartreuse4'), woods)
        if garden[y][x] == 'S':
            start = (x,y)

level = level.convert()

screen.blit(level, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()
def event_loop():
    while True:
        event = pygame.event.poll() # get event immediately, if any
        # Allow for ways to exit the application
        if event.type == pygame.QUIT: # closing the (proverbial) window
            pygame.quit(); exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
            pygame.quit(); exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            break

        clock.tick(60)

event_loop()

def visrep(squares):
    for square in squares:
        x, y = square
        gnome = pygame.Rect(x*S, y*S, S, S)
        pygame.draw.rect(screen, pygame.Color('firebrick4'), gnome)
    pygame.display.flip()
    clock.tick(30)

    for square in squares:
        x, y = square
        gnome = pygame.Rect(x*S, y*S, S, S)
        pygame.draw.rect(screen, pygame.Color('black'), gnome)


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
    x, y = dir
    t = garden[y][x]
    return t != '#'

def directions(pos):
    n = tuple(north + array(pos))
    s = tuple(south + array(pos))
    e = tuple(east  + array(pos))
    w = tuple(west  + array(pos))

    return [n, e, w, s]

def mapper(squares : list):
    new = set()

    for pos in squares:
        dirs = directions(pos)

        # dont go out of bounds
        dirs = list(filter(lambda dir: inside(dir), dirs))

        # dont backtrack
        #dirs = list(filter(lambda dir: dir not in mapped, dirs))

        # dont venture off into the woods
        dirs = list(filter(lambda dir: passable(dir), dirs))

        new.update(set(dirs))

    return new

squares = set()
for y in range(rows):
    for x in range(cols):
        if garden[y][x] == 'S':
            squares.add((x,y))

mapped = []
new = mapper(squares)
visrep(new)
for i in range(63):
    mapped += new
    new = mapper(new)
    visrep(new)

print(len(new))

event_loop()
