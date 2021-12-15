from os import path
import networkx as nx
import matplotlib.pyplot as plt
from copy import copy

lines = open("adventOfCode2021/12/input.txt", 'r').read().split()
caveSystem = nx.Graph()
caveSystem.add_edges_from([line.split(sep='-') for line in lines])

#nx.draw(caveSystem, with_labels=True)
#plt.show()

def containsDuplicates(path):
    for cave in path:
        if cave.islower() and path.count(cave) == 2:
            return True
    return False

paths = []

def scout(currentCave, path):
    global paths
    path.append(currentCave)

    # if this is a big cave we might have passed here before, if wave to the dudes standing around
    if currentCave == 'end':
        paths.append(path)
        return

    for cave in caveSystem[currentCave].keys():      
        if cave.isupper() or (cave.islower() and cave not in path) or (cave.islower() and cave != 'start' and not containsDuplicates(path)):
                # give the new scouting party my map and and make a copy for myself              
                scout(cave, copy(path))

# unleash the scouting party
scout('start', [])
print(len(paths))