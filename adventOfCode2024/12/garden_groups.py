import numpy as np


gardens = [
    'AAAA',
    'BBCD',
    'BBCC',
    'EEEC',
]

gardens = [
    'RRRRIICCFF',
    'RRRRIICCCF',
    'VVRRRCCFFF',
    'VVRCCCJFFF',
    'VVVVCJJCFE',
    'VVIVCCJJEE',
    'VVIIICJJEE',
    'MIIIIIJJEE',
    'MIIISIJEEE',
    'MMMISSJEEE',
]

from input import gardens

# read map into matrix
topology = []
for line in gardens:
    topology.append([ord(c)-65 for c in list(line)])
topology = np.array(topology)


# filter functions
def inside(pos):
    y,x = pos
    return y >= 0 and y < topology.shape[0] and x >= 0 and x < topology.shape[1]

def passable(to, fro):
    return topology[fro] == topology[to]

def directions(pos):
    north = tuple(np.array((-1, 0)) + np.array(pos))
    south = tuple(np.array(( 1, 0)) + np.array(pos))
    east  = tuple(np.array(( 0, 1)) + np.array(pos))
    west  = tuple(np.array(( 0,-1)) + np.array(pos))
    return [north, south, east, west]

def mapper(squares):
    global scan
    new = []
    for square in squares:
        y,x,_ = square
        dirs = directions((y,x))

        # dont go out of bounds
        dirs = list(filter(lambda dir: inside(dir), dirs))

        # dont climb steep hills
        dirs = list(filter(lambda dir: passable((y,x), dir), dirs))

        # update the perimeters of the region square
        square[2] -= len(dirs)

        # dont backtrack
        dirs = list(filter(lambda dir: dir not in scan, dirs))

        for direction in dirs:
            y, x = direction
            new.append([y, x, 4])

    # filter duplicates
    uniq = set([tuple(n) for n in new])
    return [list(u) for u in uniq]


scan = []
regions = []

for y in range(topology.shape[0]):
    for x in range(topology.shape[1]):
        square = (np.int64(y),np.int64(x))
        if square in scan:
            continue
        scan.append(square)

        region = [[np.int64(y),np.int64(x), 4]]
        growing = region.copy()

        while growing:

            growing = mapper(growing)
            region += growing

            path = [(y,x) for y,x,_ in growing]
            scan += path

        regions.append(region)

perimeters = [sum([c for _,_,c in region]) for region in regions]
areas = [len(region) for region in regions]

l = zip(areas, perimeters)
prices = []
for a, p in l:
    prices.append(a * p)


print(prices)

print(sum(prices))

