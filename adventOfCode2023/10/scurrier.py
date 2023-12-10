from input import path, pipes

print(f'Starting position ({path[0]})')

#directions
north = ( 0,-1)
south = ( 0, 1)
east  = ( 1, 0)
west  = (-1, 0)

# shape of pipe, where it was headed, where it goes
follower = {'L': { west  : north,
                   south : east  },
            'J': { east  : north,
                   south : west  },
            '7': { east  : south,
                   north : west  },
            'F': { west  : south,
                   north : east  },
            '-': { east  : east,
                   west  : west  },
            '|': { north : north,
                   south : south }}

# follow pipes until looped around to S
while (path[0] != path[-1]):

    # where did we come from?
    px, py = path[-2]
    x,y    = path[-1]
    dx = x - px
    dy = y - py

    # where did we go?
    pipe   = pipes[y][x]
    dx, dy = follower[pipe][(dx,dy)]
    path.append((x + dx, y + dy))

print((len(path)-1)/2)


# Ok, so lets paint it
import pygame

# figure out the canvas
S = SCALING = 3
HEIGHT = len(pipes) * S * 3
WIDTH  = len(pipes[0]) * S * 3

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

while(True):
    event = pygame.event.poll()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
        break

# expand the pipe shapes into 3x3 squares
pipe_shapes = { 'L': [pygame.Rect(S, 0, S, 2*S), pygame.Rect(2*S, S, S, S) ],
                'J': [pygame.Rect(S, 0, S, 2*S), pygame.Rect(  0, S, S, S) ],
                '7': [pygame.Rect(0, S, 2*S, S), pygame.Rect(S, 2*S, S, S) ],
                'F': [pygame.Rect(S, S, 2*S, S), pygame.Rect(S, 2*S, S, S) ],
                '-': [pygame.Rect(0, S, 3*S, S)],
                '|': [pygame.Rect(S, 0, S, 3*S)] }

loop = []
for point in path:
    x, y = point

    #pipe_pixel = pygame.Rect(x * S, y * S, S, S)
    #pygame.draw.rect(screen, (0,255,0), pipe_pixel)

    pipe = pipes[y][x]
    for pipe_shape in pipe_shapes[pipe]:
        p = pipe_shape.move(x*3*S,y*3*S)
        loop.append(p)
        pygame.draw.rect(screen, (0,255,0), p)

    pygame.display.flip()

    clock.tick()

# At this point the circular pipe has been painted
# and it's time to map all reachable squares
# Note: code borrowed from AoC 2022 12 ice_climber.py

from numpy import array

# filter functions
def inside(pos):
    x,y = pos
    return y >= 0 and y <= len(pipes) and x >= 0 and x <= len(pipes[0])

def passable(to, fro):
    to_x,  to_y  = to
    fro_x, fro_y = fro

    left = 3.0 * min([to_x, fro_x])
    top  = 3.0 * min((to_y, fro_y))

    width  = 1 + 3.0 * abs(to_x - fro_x)
    height = 1 + 3.0 * abs(to_y - fro_y)

    step = pygame.Rect(S*left, S*top, S*width, S*height)

    collides = step.collidelist(loop)

    if (collides == -1):
        pygame.draw.rect(screen, (255,0,0), step)
        pygame.display.flip()
        return True

    return False


def directions(pos):
    north = tuple(array((-1, 0)) + array(pos))
    south = tuple(array(( 1, 0)) + array(pos))
    east  = tuple(array(( 0, 1)) + array(pos))
    west  = tuple(array(( 0,-1)) + array(pos))
    return [north, south, east, west]


def mapper(squares):
    new = []
    for square in squares:
        y,x,c = square
        dirs = directions((y,x))

        # dont go out of bounds
        dirs = list(filter(lambda dir: inside(dir), dirs))

        # dont backtrack
        path = [(y,x) for y,x,_ in scan]
        dirs = list(filter(lambda dir: dir not in path, dirs))

        # dont climb steep hills # Update: don't pass through pipes
        dirs = list(filter(lambda dir: passable(dir, (y,x)), dirs))

        for direction in dirs:
            y, x = direction
            new.append((y, x, c + 1))

    return list(set(new))

# start from the endpoint and map all, reachable, squares and count the steps needed
y,x = (len(pipes)/2,len(pipes[0])/2)
#x,y = (2,6)
c = 0
scan = [(y,x,c)]

# each mapper fills in the squares directly reachable from the current squares not yet mapped
new = mapper(scan)
while(new): # stop when we can't reach any more squares
    scan += new
    new = mapper(new)
    pygame.display.flip()

pygame.display.flip()

# remove the squares with pipes from the mapping list of coordinates
scanned = [(x,y) for x,y,_ in scan]
reached = list(filter(lambda coord: coord not in path, scanned))

print(len(reached))

for square in reached:
    x,y = square
    pygame.draw.rect(screen, (255,255,0),pygame.Rect((1+x*3)*S, (1+y*3)*S, 2*S, 2*S))
    pygame.display.flip()
    pass

# remove the outside perimeter
#reached = list(filter(lambda coord: coord[0] < len(pipes[0]), reached ))
#reached = list(filter(lambda coord: coord[1] < len(pipes), reached ))

#print( len(pipes)*len(pipes[0]) - (len(path)-1) - len(reached) )

while True:
    event = pygame.event.poll() # get event immediately, if any
    # Allow for ways to exit the application
    if event.type == pygame.QUIT: # closing the (proverbial) window
        pygame.quit(); exit()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        pygame.quit(); exit()

    clock.tick(60)
