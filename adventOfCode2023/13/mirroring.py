from example import landscape
import numpy as np

def pretty_print(plot_of_land):
    byte_strings = np.apply_along_axis(b''.join, axis=1, arr=plot_of_land)

    for i in range(byte_strings.shape[0]):
        print(byte_strings[i].decode('utf-8'))


def find_reflection(plot):
    rows = plot.shape[1]

    for symmetry in range(1, int((rows-1)/2)):
        subplot = plot[0:symmetry]
        mirror  = np.flip(plot[symmetry:symmetry*2])

        pretty_print(np.stack(subplot, mirror))

        if (subplot == mirror):
            return symmetry

    return 0




for plot in landscape:
    pretty_print(plot)

    symmetry = find_reflection(plot)

    if (symmetry == 0):
        symmetry = find_reflection(plot.transpose())

    print(symmetry)



