from example import trails

rows = len(trails)
cols = len(trails[0])

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

        #dirs = list(filter(lambda dir: longer(dir,c), dirs))

        # dont venture off into the woods
        dirs = list(filter(lambda dir: passable(dir), dirs))

        if not dirs:
            dead.append(path) # this is where the journey ends, we wil keep stepping in place until all journeys end
            continue

        new = True # we've taken a step in one or more directions

        # if we're merely continuing on the path, then add this one step
        if len(dirs) >= 1:
            x,y = dirs[0]
            path.append((x, y, c + 1))
            fro.append(path)

        # at this point we need to clone ourselves and continue in more than one direction
        for i in range(1, len(dirs)):
            x,y = dirs[i]
            clone = path.copy()
            clone.append((x, y, c + 1))
            fro.append(clone)

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
paths = [[(cols-2, rows-1, 0)]]

# each mapper fills in the squares directly reachable from the current squares not yet mapped
new, paths, dead = mapper(paths, [])

pretty_print(paths, dead)
while(new): # stop when we can't reach any more squares
    new, paths, dead = mapper(paths, dead)
    #pretty_print(paths, dead)

pretty_print(paths, dead)

journey_lengths = []
for path in dead:
    x,y,c = path[-1]
    if x == 1 and y == 0:
        journey_lengths.append(c)

print(journey_lengths)
print(max(journey_lengths))
