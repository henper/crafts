from input import trails
from itertools import pairwise
import networkx as nx
import pygame

G = nx.Graph()

rows = len(trails)
cols = len(trails[0])

start = (1, 0)
goal  = (cols-2, rows-1)

# figure out the canvas
S = SCALING = 5
HEIGHT = rows * S
WIDTH  = cols * S

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
level = pygame.Surface((WIDTH, HEIGHT))

for y in range(rows):
    for x in range(cols):
        if trails[y][x] == '#':
            woods = pygame.Rect(x*S, y*S, S, S)
            pygame.draw.rect(level, pygame.Color('chartreuse4'), woods)
level = level.convert()

screen.blit(level, (0,0))
pygame.display.flip()

hiker_colors = [
    pygame.Color('firebrick1'),
    pygame.Color('firebrick2'),
    pygame.Color('firebrick3'),
    pygame.Color('firebrick4'),
    pygame.Color('black')
]

clock = pygame.time.Clock()
def event_loop():
    while True:
        event = pygame.event.poll() # get event immediately, if any
        # Allow for ways to exit the application
        if event.type == pygame.QUIT: # closing the (proverbial) window
            pygame.quit(); exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
            pygame.quit(); exit()

        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    break

        clock.tick(60)

def visrep(paths, dead):
    for path in paths:
        if len(path) >= len(hiker_colors):
            for i in range(1,len(hiker_colors)+1):
                x, y = path[-i]
                hiker = pygame.Rect(x*S, y*S, S, S)
                pygame.draw.rect(screen, hiker_colors[i-1], hiker)

    for path in dead:
        x, y = path[-1]
        hiker = pygame.Rect(x*S, y*S, S, S)
        pygame.draw.rect(screen, pygame.Color('firebrick4'), hiker)
    pygame.display.flip()
    clock.tick(60)

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
    x, y = dir
    t = trails[y][x]
    return t != '#'

def directions(pos):
    n = tuple(north + array(pos))
    s = tuple(south + array(pos))
    e = tuple(east  + array(pos))
    w = tuple(west  + array(pos))

    return [n, e, w, s]

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
        pos = path[-1]
        dirs = directions(pos)

        # dont go out of bounds
        dirs = list(filter(lambda dir: inside(dir), dirs))

        # dont backtrack
        dirs = list(filter(lambda dir: dir not in path, dirs))

        # dont venture off into the woods
        dirs = list(filter(lambda dir: passable(dir), dirs))

        if not dirs:
            # this is where the journey ends
            G.add_node(pos)
            G.add_edge(pos, path[0], weight = len(path), trail = path)
            continue

        new = True # we've taken a step in one or more directions

        # if we're merely continuing on the path, then add this one step and continue walking
        if len(dirs) == 1:
            path.append(dirs[0])
            fro.append(path)
            continue

        # When the path forks add the current location as a node and add more mappers

        if pos in G:
            G.add_edge(pos, path[0], weight = len(path), trail = path)
            continue # node has already been mapped, others will take care of it. Lay down and rest.

        # and an edge from the path we took to get here
        G.add_node(pos)
        G.add_edge(pos, path[0], weight = len(path), trail = path)

        # at this point we need to continue in more than one direction
        for i in range(0, len(dirs)):
            fro.append([pos, dirs[i]])

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
paths = [[goal]]
G.add_node(goal)

# each mapper fills in the squares directly reachable from the current squares not yet mapped
new, paths, dead = mapper(paths, [])

visrep(paths, dead)
while(new): # stop when we can't reach any more squares
    new, paths, dead = mapper(paths, dead)
    visrep(paths, dead)

path_weights = []
simple_paths = list(nx.all_simple_paths(G, start, goal))
for path in simple_paths:
    path_weights.append(nx.path_weight(G, path, weight="weight") - (len(path) - 1))
print(max(path_weights))

import matplotlib.pyplot as plt
layout = nx.spring_layout(G)
nx.draw_networkx_nodes(G, layout)
nx.draw_networkx_labels(G, layout)
nx.draw_networkx_edges(G, layout)
nx.draw_networkx_edge_labels(G, layout, nx.get_edge_attributes(G, "weight"))
plt.show()

for edge in pairwise(simple_paths[path_weights.index(max(path_weights))]):
    a,b = edge
    trail = G[a][b]['trail']

    if trail[0] != a:
        trail.reverse()

    for x,y in trail:
            hiker = pygame.Rect(x*S, y*S, S, S)
            pygame.draw.rect(screen, pygame.Color('gold'), hiker)
            pygame.display.flip()
            clock.tick(120)

event_loop()
