from itertools import permutations
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import numpy as np

from example import hail_stones
limits = (200000000000000, 400000000000000)
limits = (7,27)

# figure out the equation, y = k*x + m for each hail stone
trajectories = []
for hail_stone  in hail_stones:
    pos, delta = hail_stone
    x,y,_ = pos
    dx, dy, _ = delta

    k = dy / dx

    m = y - k * x

    # determine end-point
    end_x = max(limits) if dx > 0 else min(limits)
    end_y = k * end_x + m

    #if end_y > max(limits):
    #    end_y = max(limits)
    #    end_x = (end_y - m) / k

    if end_y < min(limits):
        end_y = min(limits)
        end_x = (end_y - m) / k

    trajectories.append((pos, (end_x, end_y)))

# plot the trajectory within the given limits
ax = plt.subplot()

rect = patches.Rectangle((min(limits), min(limits)), max(limits)-min(limits), max(limits)-min(limits), linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rect)

paths = []
for traj in trajectories:
    pos, end = traj

    '''
    if k > 0:
        ys = [y, k*max(limits)+m]
        xs = [x, max(limits)]
    else:
        ys = [k*min(limits)+m, y]
        xs = [min(limits), x]
    '''

    xs = [pos[0], end[0]]
    ys = [pos[1], end[1]]

    plt.plot(xs, ys, '.-')

plt.legend(['area', 'A', 'B', 'C', 'D', 'E'])
plt.xlabel('x')
plt.ylabel('y')
#plt.xlim(limits)
#plt.ylim(limits)
plt.show()

# pair each hailstone up with every other stone, and determine if their future paths will cross
for pair in permutations(trajectories, 2):
    a, b = pair





