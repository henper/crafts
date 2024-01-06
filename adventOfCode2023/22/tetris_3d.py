from input import bricks

from functools import cmp_to_key
import matplotlib.pyplot as plt
import numpy as np

# figure out the space we're working with
shape = [0,0,0]
for brick in bricks:
    start, end = brick

    sx, sy, sz = start
    ex, ey, ez = end

    shape[0] = max(shape[0], sx, ex)
    shape[1] = max(shape[1], sy, ey)
    shape[2] = max(shape[2], sz, ez)

shape = np.array(shape) + 1

# fill in the voxels of each brick
voxel_bricks = []
for brick in bricks:
    voxel_bricks.append([])

    # x differs
    if brick[0][0] != brick[1][0]:
        y = brick[0][1]
        z = brick[0][2]
        for x in range(brick[0][0], brick[1][0] + 1):
            voxel_bricks[-1].append([x,y,z])
        continue

    # y differs
    if brick[0][1] != brick[1][1]:
        x = brick[0][0]
        z = brick[0][2]
        for y in range(brick[0][1], brick[1][1] + 1):
            voxel_bricks[-1].append([x,y,z])
        continue

    # z differs
    if brick[0][2] != brick[1][2]:
        x = brick[0][0]
        y = brick[0][1]
        for z in range(brick[0][2], brick[1][2] + 1):
            voxel_bricks[-1].append([x,y,z])
        continue

    # brick is a single voxel
    x = brick[0][0]
    y = brick[0][1]
    z = brick[0][2]
    voxel_bricks[-1].append([x,y,z])

def lower(a, b):
    a = min([z for _,_,z in a])
    b = min([z for _,_,z in b])
    return a - b

voxel_bricks = sorted(voxel_bricks, key=cmp_to_key(lower))


def bricks2voxels(bricks):
    voxels = np.zeros(shape)
    db = {}

    for brick in bricks:
        for x,y,z in brick:
            voxels[x][y][z] = 1
            db[(x,y,z)] = tuple(map(tuple, brick))
    return voxels, db

def visrep(voxels, colors=None):

    ax = plt.figure().add_subplot(projection='3d')


    ax.voxels(filled=voxels, facecolors=colors, edgecolor='k')
    ax.set_zlim(1, 11)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

#voxel_bricks = list(filter(lambda brick: max([z for _,_,z in brick]) < 9, voxel_bricks))
#voxel_bricks = list(filter(lambda brick: max([z for _,_,z in brick]) > 6, voxel_bricks))

voxels, db = bricks2voxels(voxel_bricks)
#visrep(voxels)

def drop(xrange, yrange, zrange):

    z_min = 1
    hits = []

    for z in zrange:
        for y in yrange:
            for x in xrange:
                if voxels[x][y][z] > 0:
                    z_min = z + 1
                    hits.append((x,y,z))
        if len(hits) > 0:
            break

    return (z_min, hits)

def drop_all(bricks):
    # from bottom to top, find bricks col by col, row by row and drop'em
    dropped_bricks = []
    essentials = set()

    for z in range(shape[2]):
        for y in range(shape[1]):
            for x in range(shape[0]):

                if voxels[x][y][z] == 0:
                    continue

                for brick in bricks:
                    if [x,y,z] in brick:

                        for voxel in brick:
                            # set old location as void
                            vx,vy,vz = voxel
                            voxels[vx][vy][vz] = 0
                            del db[vx,vy,vz]

                        # Search straight down for all x's and y's in the brick until we hit something
                        xrange = range(min([x for x,_,_ in brick]), max([x for x,_,_ in brick]) + 1)
                        yrange = range(min([y for _,y,_ in brick]), max([y for _,y,_ in brick]) + 1)
                        zrange = range(min([z for _,_,z in brick]), 0, -1)

                        z_min, hits = drop(xrange, yrange, zrange)

                        supports = []
                        for hit in hits:
                            supports.append(db[hit])

                        if len(supports) > 1:
                            slist = [supports[0]] * len(supports)
                            if slist == supports:
                                essentials.add(db[hit])
                        if len(supports) == 1:
                            essentials.add(db[hit])

                        dropped = []
                        if len(xrange) == 1 and len(yrange) == 1:
                            for dx,dy,_ in brick:
                                # set new location
                                voxels[dx][dy][z_min] = 1
                                dropped.append([dx,dy,z_min])
                                z_min += 1

                        else:
                            for dx,dy,_ in brick:
                                # set new location
                                voxels[dx][dy][z_min] = 1
                                dropped.append([dx,dy,z_min])

                        for dx,dy,dz in dropped:
                            db[(dx,dy,dz)] = tuple(map(tuple, dropped))

                        dropped_bricks.append(dropped)
                        bricks.pop(bricks.index(brick))

                        break

    return dropped_bricks, essentials

dropped_bricks, essentials = drop_all(voxel_bricks)

e_voxels, _ = bricks2voxels(essentials)

colors = np.empty(voxels.shape, dtype=object)
colors[:] = 'blue'

colors[np.where(e_voxels)] = 'red'

visrep(voxels, colors)

print(len(bricks))
print(len(essentials))

def calc_supporting(brick, tower : set):
    # Find all bricks that are supported by this one..
    supporting = set()

    # Search one step up for all x's and y's in the brick
    xrange = range(min([x for x,_,_ in brick]), max([x for x,_,_ in brick]) + 1)
    yrange = range(min([y for _,y,_ in brick]), max([y for _,y,_ in brick]) + 1)
    z = max([z for _,_,z in brick]) + 1

    for y in yrange:
        for x in xrange:
            if (x,y,z) in db.keys():
                supported = db[(x,y,z)]

                # ..and only this brick, if the one above it is supported by another brick as well then it doesn't count
                voxels = [(x,y,z-1) for (x,y,z) in supported] # volume below the brick in question
                voxels = list(filter(lambda voxel: voxel not in supported, voxels)) # remove voxels that are part of the same brick (for standing bricks)
                voxels = list(filter(lambda voxel: voxel not in brick, voxels)) # remove all voxels that belong to the support in question
                if all(voxel not in db.keys() for voxel in voxels):
                    supporting.add(db[(x,y,z)])
                    continue

                # well, it can be supported by more than this brick in question, if they are all part of the same system aka. tower
                supports = set()
                for voxel in voxels:
                    if voxel in db.keys():
                        supports.add(db[voxel])

                pillars = supports.difference(tower)
                if not pillars:
                    supporting.add(db[(x,y,z)])

    # Add all the supported bricks to this tower
    tower.update(supporting)

    # Then recursively figure out which bricks they in turn supports
    for supported in supporting.copy():
        supporting.update(calc_supporting(supported, tower))

    return supporting

answer = 0
for brick in essentials:
    answer += len((calc_supporting(brick, set())))


print(answer)