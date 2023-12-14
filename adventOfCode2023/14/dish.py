from input import platform
import numpy as np

def pretty_print(plot_of_land):
    byte_strings = np.apply_along_axis(b''.join, axis=1, arr=plot_of_land)

    hashable = str()
    for i in range(byte_strings.shape[0]):
        hashable += byte_strings[i].decode('utf-8')
        hashable += '\n'
    return hashable

def tip(platform):

    #print(pretty_print(platform))

    rows, cols = platform.shape

    for col in range(cols):
        slice = platform[:, col]

        # find the indices of all rocks (and unpack from tuple)
        rollers  = np.where(slice == b'O')[0]
        stoppers = np.where(slice == b'#')[0]

        # build a new array which will contain all the rocks after rolling
        slice = np.array(np.frombuffer(b'.' * rows, dtype='S1'))
        slice[stoppers] = b'#' # stoppers doesn't move

        top = 0
        for roller in rollers.tolist():

            # is there a stopper that will block us?
            if (stoppers <= roller).any():
                blockers = stoppers * (stoppers <= roller)
                if blockers.size > 0:
                    blocker = np.max(blockers)
                    if blocker >= top:
                        top = blocker + 1

            # put roller at the top
            slice[top] = b'O'
            top += 1

        # replace the original column with the new slice
        platform[:, col] = slice
    return platform


def spin_cycle(platform):
    #north
    tip(platform)

    #west
    platform = platform.transpose()
    tip(platform)
    platform = platform.transpose()

    # south
    platform = np.flip(platform, axis=0)
    tip(platform)
    platform = np.flip(platform, axis=0)

    # east
    platform = np.flip(platform.transpose(), axis=0)
    tip(platform)
    platform = np.flip(platform, axis=0).transpose()

# Spin until we find a spot that repeats
cache = {}
spin_cycles = 0
while True:
    cache[pretty_print(platform)] = spin_cycles

    spin_cycle(platform)
    spin_cycles += 1

    if pretty_print(platform) in cache.keys():
        break


# From 0 spins to to the repetition point
loop_begin = cache[pretty_print(platform)]
loop_end   = spin_cycles
loop_len   = loop_end - loop_begin

# Fast forward
remaining_cycles = (1000000000 - loop_begin) % loop_len

print(f'loop begin: {loop_begin}, end {loop_end}, length {loop_len}, remaining {remaining_cycles}')

for i in range(remaining_cycles):
    spin_cycle(platform)

# Weigh in
rows, cols = platform.shape

weights = np.array([[weight] * cols for weight in range(rows, 0, -1)])
print(np.sum((platform == b'O') * weights))
