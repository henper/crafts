import numpy as np
from copy import copy

input = open("adventOfCode2022/12/input.txt", 'r').read().split()
start = (20,  0)
end   = (20, 36)
"""
input = open("adventOfCode2022/12/example.txt", 'r').read().split()
start = (0,0)
end   = (2,5)
"""

# read map into matrix
topology = []
for line in input:
    topology.append([ord(c)-97 for c in list(line)])
topology = np.array(topology)

# replace tokens with heights
topology[start] =  0
topology [end]  = 26

# filter functions
def inside(pos, shape):
    y,x = pos
    return y >= 0 and y < topology.shape[0] and x >= 0 and x < topology.shape[1]

steps = []
def climber(pos, path, ever):
    global paths

    if pos == end:
        print(path)
        steps.append(len(path))
        return

    path.append(pos)

    north = tuple(np.array((-1, 0)) + np.array(pos))
    south = tuple(np.array(( 1, 0)) + np.array(pos))
    east  = tuple(np.array(( 0, 1)) + np.array(pos))
    west  = tuple(np.array(( 0,-1)) + np.array(pos))
    directions = [north, south, east, west]

    # dont go out of bounds
    directions = list(filter(lambda dir: inside(dir, topology.shape), directions))

    # dont backtrack
    directions = list(filter(lambda dir: dir not in path, directions))

    height = topology[path[-1]]
    for direction in directions:
        if height + 1 >= topology[direction]:
            climber(direction, copy(path))
    del path


climber(start, [])

steps.sort()
print(steps[0])
