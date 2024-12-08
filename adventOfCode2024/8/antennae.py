from itertools import combinations

city = [
    'T....#....',
    '...T......',
    '.T....#...',
    '.........#',
    '..#.......',
    '..........',
    '...#......',
    '..........',
    '....#.....',
    '..........',
]

city = [
    #012345678901
    '......#....#', #  0
    '...#....0...', #  1
    '....#0....#.', #  2
    '..#....0....', #  3
    '....0....#..', #  4
    '.#....A.....', #  5
    '...#........', #  6
    '#......#....', #  7
    '........A...', #  8
    '.........A..', #  9
    '..........#.', # 10
    '..........#.', # 11
]


from input import city

blocks  = len(city)
streets = len(city[0])

# determine the frequencies
frequencies = set()
for block in city:
    frequencies.update(' '.join(block).split())

frequencies.remove('.')

'''
frequencies.remove('#')

facit = []
for block in range(blocks):
        for street in range(streets):
            if city[block][street] == '#':
                facit.append((block,street))
'''

# find the coordinates of all frequencies
antennae = dict()
for frequency in frequencies:
    antennae[frequency] = []
    for block in range(blocks):
        for street in range(streets):
            if city[block][street] == frequency:
                antennae[frequency].append((block,street))

# determine the antinode of all antenna pairs
antinode = []
for antenna in antennae.values():
    pairs = list(combinations(antenna, 2))

    for pair in pairs:
        # cartesian distance
        a,b = pair
        ax, ay = a
        bx, by = b

        dx = ax - bx
        dy = ay - by

        # place an antinode at each antenna
        antinode.append(a)
        antinode.append(b)

        # add the resonant and harmonic nodes, that are inside the city
        def inside_city(nx, ny):
            return ny >= 0 and ny < blocks and nx >= 0 and nx < streets

        nx, ny = ax+dx, ay+dy
        while (inside_city(nx, ny)):
            antinode.append((nx, ny))
            nx += dx
            ny += dy

        nx, ny = bx-dx, by-dy
        while (inside_city(nx, ny)):
            antinode.append((nx, ny))
            nx -= dx
            ny -= dy

print(len(set(antinode)))
