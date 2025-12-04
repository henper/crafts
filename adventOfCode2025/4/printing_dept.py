import numpy as np

from example import grid

# read grid into matrix
topology = []
for line in grid:
    topology.append(list(line))
topology = np.array(topology)

def directions(pos):
    north = tuple(np.array((-1, 0)) + np.array(pos))
    south = tuple(np.array(( 1, 0)) + np.array(pos))
    east  = tuple(np.array(( 0, 1)) + np.array(pos))
    west  = tuple(np.array(( 0,-1)) + np.array(pos))

    north_east = tuple(np.array((-1, 1)) + np.array(pos))
    south_east = tuple(np.array(( 1, 1)) + np.array(pos))
    south_west = tuple(np.array(( 1,-1)) + np.array(pos))
    north_west = tuple(np.array((-1,-1)) + np.array(pos))
    return [north, south, east, west, north_east, south_east, south_west, north_west]

def inside(pos):
    y,x = pos
    return y >= 0 and y < topology.shape[0] and x >= 0 and x < topology.shape[1]

def occupied(dir):
    return topology[dir] == '@'


grabbable = 0

for y in range(topology.shape[0]):
    for x in range(topology.shape[1]):
        if topology[y,x] == '.':
            print('.', end='')
            continue

        neighbors = directions((y,x))

        neighbors = list(filter(lambda pos: inside(pos), neighbors))

        neighbors = list(filter(lambda dir: occupied(dir), neighbors))

        if len(neighbors) >= 4:
            print('@', end='')
        else:
            print('x', end='')
            grabbable += 1



    print()

print(f"Grabbable rolls: {grabbable}")
