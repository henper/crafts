from input import contraption
rows = len(contraption[0])
cols = len(contraption)

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

paths = [[((0,0), east)]]

def move(path, heading):
    location,_ = path[-1]
    x,y = location
    dx, dy = heading

    location = (x+dx, y+dy)
    x,y = location

    # dont go out of bounds
    if 0 <= x and x < rows and 0 <= y and y < cols:

        # dont go back on yourself in the same direction
        if (location, heading) not in path:

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


traverse(paths[0])

energized = set()
for path in paths:
    path = [(x,y) for ((x,y),_) in path]
    path = set(path)

    energized.update(path)

print(len(energized))


for y, row in enumerate(contraption):
    row += ' '
    for x in range(rows):
        if (x, y) in energized:
            row += '#'
        else:
            row += contraption[y][x]
    print(row)
