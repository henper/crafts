import numpy as np

from input import grid

# read grid into matrix
def grid2mat(grid):
    topology = []
    for line in grid:
        topology.append(list(line))
    topology = np.array(topology)
    return topology

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


def grabbable(topology):
    count_grabbable = 0
    new_topo = topology.copy()
    for y in range(topology.shape[0]):
        for x in range(topology.shape[1]):
            if topology[y,x] == '.' or topology[y,x] == 'x':
                #print('.', end='')
                continue

            neighbors = directions((y,x))

            neighbors = list(filter(lambda pos: inside(pos), neighbors))

            neighbors = list(filter(lambda dir: occupied(dir), neighbors))

            if len(neighbors) >= 4:
                pass
                #print('@', end='')
            else:
                new_topo[y,x] = 'x'
                #print('x', end='')

                count_grabbable += 1
        #print()
    return count_grabbable, new_topo

topology = grid2mat(grid)

count_grabbable, new_topo = grabbable(topology)
print(f"Grabbable rolls: {count_grabbable}")

tot_grabbable = count_grabbable

while count_grabbable > 0:
    topology = new_topo
    count_grabbable, new_topo = grabbable(topology)
    tot_grabbable += count_grabbable
    print(f"Grabbable rolls: {count_grabbable}")
print(f"Total grabbable rolls: {tot_grabbable}")
