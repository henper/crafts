from input import pipes


path = []

# find S(currier)
for y, line in enumerate(pipes):
    if 'S' in line:
        x = line.index('S')
        path.append((x,y))
        break

print(f'Starting position ({path[0]})')

# from S pick a direction TODO (or you know, just hardcode it)
#path.append((2,1))
path.append((24,83))

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


