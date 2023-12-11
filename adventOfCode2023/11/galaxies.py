
import numpy as np
import itertools

from example import image

# Expand galaxy

# find rows and cols without galaxies, and insert a row or column with more empty space
rows, cols = image.shape

image_copy = image.copy()

insertions = 0
for row, empty_space in enumerate(np.sum(image == b'.', axis=0) == rows):
    if (empty_space):
        image_copy = np.insert(image_copy, row + insertions, b'.', axis=1)
        insertions += 1

insertions = 0
for col, empty_space in enumerate(np.sum(image == b'.', axis=1) == cols):
    if (empty_space):
        image_copy = np.insert(image_copy, col + insertions, b'.', axis=0)
        insertions += 1

# list all coordinates of galaxies
galaxies = np.transpose((image_copy == b'#').nonzero())
pairs = list(itertools.combinations(galaxies, 2))


answer = 0

for pair in pairs:
    ay, ax = pair[0]
    by, bx = pair[1]

    distance = abs(ay - by) + abs(ax - bx)
    answer += distance

print(answer)
