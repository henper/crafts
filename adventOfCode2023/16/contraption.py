from input import contraption
rows = len(contraption[0])
cols = len(contraption)
print(f'rows: {rows}, cols: {cols}')

import sys
print(sys.getrecursionlimit())
#sys.setrecursionlimit(10000)

#directions
north = ( 0,-1)
south = ( 0, 1)
east  = ( 1, 0)
west  = (-1, 0)

# shape of pipe, where it was headed, where it goes
follower = {'\\': { east  : [south], west : [north],
                    north : [west], south : [east] },
            '/' : { west  : [south], east : [north],
                    north : [east], south : [west] },
            '.' : {},
            '-' : { north : [east, west],
                    south : [east, west] },
            '|' : { east  : [north, south],
                    west  : [north, south] }}

paths = [[]]

def move(path, heading):
    location,_ = path[-1]
    x,y = location
    dx, dy = heading

    location = (x+dx, y+dy)
    x,y = location

    if 0 > x or x >= rows or 0 > y or y >= cols:
        return

    while contraption[y][x] == '.':

        path.append(((x, y), heading))

        x += dx
        y += dy

        if 0 > x or x >= rows or 0 > y or y >= cols:
            return



    # dont go out of bounds
    if 0 <= x and x < rows and 0 <= y and y < cols:
        location = (x,y)

        # dont go back on yourself in the same direction
        if (location, heading) not in path:

            for p in paths:
                if (location, heading) in p:
                    return

            path.append((location, heading))
            traverse(path)

def traverse(path):
    location, heading = path[-1]
    x,y = location

    part = contraption[y][x]

    if heading in follower[part].keys():
        headings = follower[part][heading]
    else:
        headings = [heading]

    if len(headings) == 2:

        split = path.copy()

        paths.append(split)

        move(split, headings[1])

    move(path, headings[0])

def calc_energized():
    energized = set()
    for path in paths:
        path = [(x,y) for ((x,y),_) in path]
        path = set(path)

        energized.update(path)
    return energized

def pretty_print(energized):
    return
    for y, row in enumerate(contraption):
        row += ' '
        for x in range(rows):
            if (x, y) in energized:
                row += '#'
            else:
                row += contraption[y][x]
        print(row)

num_energized = []

# it came from the west
for y in range(rows):
    paths.clear()
    paths.append([])
    paths[0].append(((0,y), east))
    traverse(paths[0])
    energized = calc_energized()
    pretty_print(energized)
    num_energized.append(len(energized))
    print(f'westbound row {y} energized {num_energized[-1]}')

# it came from the south
for x in range(cols):
    paths.clear()
    paths.append([])
    paths[0].append(((x,rows-1), north))
    traverse(paths[0])
    energized = calc_energized()
    pretty_print(energized)
    num_energized.append(len(energized))
    print(f'northound col {x} energized {num_energized[-1]}')

# it came from the east
for y in range(rows):
    paths.clear()
    paths.append([])
    paths[0].append(((cols-1, y), west))
    traverse(paths[0])
    energized = calc_energized()
    pretty_print(energized)
    num_energized.append(len(energized))
    print(f'eastbound col {y} energized {num_energized[-1]}')

# it came from the north
for x in range(cols):
    paths.clear()
    paths.append([])
    paths[0].append(((x,0), south))
    traverse(paths[0])
    energized = calc_energized()
    pretty_print(energized)
    num_energized.append(len(energized))
    print(f'southound col {x} energized {num_energized[-1]}')



print(max(num_energized))
