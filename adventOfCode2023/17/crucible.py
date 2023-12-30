from example import city

from numpy import array
rows = len(city)
cols = len(city[0])

north = ( 0,-1)
south = ( 0, 1)
east  = ( 1, 0)
west  = (-1, 0)


# filter functions
def inside(pos):
    x,y = pos
    return y >= 0 and y < rows and x >= 0 and x < cols

def passable(to, fro, tango: list):
    # determine direction
    dir = tuple(array(to) - array(fro))

    # cannot be the same as the two previous steps in the tango
    return not [dir] * 2 == tango

def directions(pos):
    n = tuple(array(north) + array(pos))
    s = tuple(array(south) + array(pos))
    e = tuple(array(east)  + array(pos))
    w = tuple(array(west)  + array(pos))
    return [n, s, e, w]


def mapper(squares):
    new = []
    for square in squares:
        x,y,c,t = square
        dirs = directions((x,y))

        # dont go out of bounds
        dirs = list(filter(lambda dir: inside(dir), dirs))

        # dont climb steep hills # Update: don't continue in the same direction thrice
        dirs = list(filter(lambda dir: passable(dir, (x,y), t), dirs))

        t.pop(0)

        for direction in dirs:
            y, x = direction
            nc = c + int(city[y][x])

            nt = t.copy()
            nt.append(direction)

            sc, st = scan[y][x]
            if sc == -1 or (sc > c and st == nt):
                new.append((x, y, nc, nt))
                continue

                locs = [(x,y) for x,y,_,_ in new]
                if (x,y) in locs:
                    # replace a new item with this one if cheaper
                    i = locs.index((x,y))
                    _, _, nc,ot = new[i]
                    if nc > c and ot == nt:
                        new[i] = (x, y, nc, nt)
                    else:
                        new.append((x, y, nc, nt))
                else:
                    new.append((x, y, nc, nt))

    return new


def pretty_print(squares):
    map = [['..'] * cols for r in range(rows)]

    for square in squares:
        x, y, c,_ = square
        map[y][x] = format(c, '2d')

    for row in map:
        print(" ".join(row))

    print('')




x = y = c = 0
tango = [east, north] # initialize the 2-step tango to allow for any direction
scan = [([(-1, [])] * cols) for r in range(rows)]

# each mapper fills in the squares directly reachable from the current squares not yet mapped
new = mapper([(x,y,c, tango)])
pretty_print(new)

while(new): # stop when we can't reach any more squares

    for x,y,c,t in new:
        scan[y][x] = (c,t)

    new = mapper(new)

    pretty_print(new)

print(scan[rows-1][cols-1])
