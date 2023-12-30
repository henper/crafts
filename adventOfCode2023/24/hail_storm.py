from itertools import combinations
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import numpy as np

from input import hail_stones
limits = (200000000000000, 400000000000000)
#limits = (7,27)

class Coord():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y

class Hail():
    def __init__(self, pos, delta) -> None:
        x,y,_ = pos
        dx, dy, _ = delta

        self.pos = Coord(x,y)

        # figure out the equation, y = k*x + m for each hail stone
        k = dy / dx
        m = y - k * x

        self.k = k
        self.m = m

        # determine the start-point, the given position or where the line segment enters the limits
        if x < min(limits) or x > max(limits):
            x = max(limits) if x > max(limits) else min(limits)
            y = k * x + m

        if y < min(limits) or y > max(limits):
            y = max(limits) if y > max(limits) else min(limits)
            x = (y - m) / k

        # determine end-point
        end_x = max(limits) if dx > 0 else min(limits)
        end_y = k * end_x + m

        if end_y < min(limits) or end_y > max(limits):
            end_y = max(limits) if end_y > max(limits) else min(limits)
            end_x = (end_y - m) / k

        self.start = Coord(x,y)
        self.end   = Coord(end_x, end_y)


    def intersects(self, other, ax = None) -> bool:
        # Parallel lines never intersect
        if self.k == other.k:
            return False

        # Calculate where the two lines intersect, note that parallel lines results in divide by zero
        k = other.k / self.k
        y = (k*self.m - other.m) / (k - 1)
        x = (other.m - self.m) / (self.k - other.k)

        intersect_within_limits = min(limits) <= x and x <= max(limits) and min(limits) <= y and y <= max(limits)

        maxima = Coord(min(max(self.pos.x, self.end.x), max(other.pos.x, other.end.x)), min(max(self.pos.y, self.end.y), max(other.pos.y, other.end.y)))
        minima = Coord(max(min(self.pos.x, self.end.x), min(other.pos.x, other.end.x)), max(min(self.pos.y, self.end.y), min(other.pos.y, other.end.y)))

        intersect_in_the_future = minima.x <= x and x <= maxima.x and minima.y <= y and y <= maxima.y

        if ax is not None and intersect_in_the_future and intersect_within_limits:
            ax.plot(x,y,'xb')

        return intersect_within_limits and intersect_in_the_future



    def plot(self, ax):
        xs = [self.start.x, self.end.x]
        ys = [self.start.y, self.end.y]
        ax.plot(xs, ys, '.-')


hails = []
for hail_stone  in hail_stones:
    hails.append(Hail(*hail_stone))

# plot the trajectory within the given limits
ax = plt.subplot()

rect = patches.Rectangle((min(limits), min(limits)), max(limits)-min(limits), max(limits)-min(limits), linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rect)

paths = []
for hail in hails:
    hail.plot(ax)

# pair each hailstone up with every other stone, and determine if their future paths will cross
answer = 0
for pair in combinations(hails, 2):
    a, b = pair
    if a.intersects(b, ax):
        answer += 1

print(answer)

#plt.legend(['area', 'A', 'B', 'C', 'D', 'E'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
