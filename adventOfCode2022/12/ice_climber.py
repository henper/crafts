import numpy as np

from time import time
timestamp = time()

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
def inside(pos):
    y,x = pos
    return y >= 0 and y < topology.shape[0] and x >= 0 and x < topology.shape[1]

def passable(to, fro):
    return topology[fro] + 1 >= topology[to]

def directions(pos):
    north = tuple(np.array((-1, 0)) + np.array(pos))
    south = tuple(np.array(( 1, 0)) + np.array(pos))
    east  = tuple(np.array(( 0, 1)) + np.array(pos))
    west  = tuple(np.array(( 0,-1)) + np.array(pos))
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

        # dont climb steep hills
        dirs = list(filter(lambda dir: passable((y,x), dir), dirs))

        for direction in dirs:
            y, x = direction
            new.append((y, x, c + 1))

    return list(set(new))

# start from the endpoint and map all, reachable, squares and count the steps needed
y,x = end
c = 0
scan = [(y,x,c)]

# each mapper fills in the squares directly reachable from the current squares not yet mapped
new = mapper(scan)
while(new): # stop when we can't reach any more squares
    scan += new
    new = mapper(new)

# fill in the map, same shape as the topology, but with steps instead of heights
map = np.zeros(topology.shape, dtype=int)
for square in scan:
    y,x,c = square
    map[y,x] = c

# step 1
print(map[start])

# step 2
# not all squares are reachable so exlude the 0 steps
scenic_starts = list(set(map[np.where(topology == 0)]))
scenic_starts.sort()
print(scenic_starts[1])

print("=== %.2f seconds ===" % (time() - timestamp))
