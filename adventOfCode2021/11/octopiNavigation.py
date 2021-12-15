from os import system
import numpy as np
from scipy import signal

lines = open("adventOfCode2021/11/input.txt", 'r').read().split()

chars = list(map(list, lines))
ints = [list(map(int, l)) for l in lines]
mat = np.array(ints, int)

system('clear')

ones = np.ones(np.shape(mat), int)
kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

flashes = 0

steps = 1000
for step in range(steps):

    mat = mat + ones # energy increases by one on every position for every step

    flashed = np.zeros(np.shape(mat), int)

    # detect and propagate flashes until steady-state is reached
    org = np.zeros(np.shape(mat), int)
    while not np.array_equal(mat, org):
        org = mat.copy()

        # detect all new flashes
        flashing = 1 * (mat >= 10)

        # keep track of all that have flashed during this step
        flashed += flashing

        spread = signal.convolve2d(flashing, kernel, mode='same')
        mat = mat + spread

        # reset all that flashed during this step to zero
        mat = mat * (1 * (flashed == 0))

    if np.array_equal(flashed, ones):
        print(f'octopi synced at step: {step + 1}')
        break

    flashes += np.sum(1 * (mat == 0))

print(flashes)