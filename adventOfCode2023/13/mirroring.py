from input import landscape
import numpy as np

def pretty_print(plot_of_land):
    byte_strings = np.apply_along_axis(b''.join, axis=1, arr=plot_of_land)
    print('')
    for i in range(byte_strings.shape[0]):
        print(byte_strings[i].decode('utf-8'))


def find_reflection(plot):
    rows, cols = plot.shape

    for symmetry in range(1, -(rows // -2)): # weird looking ceil_div

        subplot = plot[0:symmetry]
        mirror  = np.flip(plot[symmetry:symmetry*2], axis=0)

        if np.sum(subplot == mirror) == symmetry*cols - 1:
            return symmetry

    return None


answer = 0

for plot in landscape:
    rows, cols = plot.shape

    # down
    ref = find_reflection(plot)
    if ref:
        answer += 100 * ref
        continue

     # up
    ref = find_reflection(np.flip(plot, axis=0))
    if ref:
        answer += 100 * (rows - ref)
        continue

    # left
    ref = find_reflection(plot.transpose())
    if ref:
        answer += ref
        continue

    # right
    ref = find_reflection(np.flip(plot.transpose()))
    if ref:
        answer += (cols - ref)
        continue

print(answer)
