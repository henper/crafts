from input import platform
import numpy as np

def pretty_print(plot_of_land):
    byte_strings = np.apply_along_axis(b''.join, axis=1, arr=plot_of_land)
    print('')
    for i in range(byte_strings.shape[0]):
        print(byte_strings[i].decode('utf-8'))


pretty_print(platform)

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

pretty_print(platform)

# Weigh in
weights = np.array([[weight] * cols for weight in range(rows, 0, -1)])
print(np.sum((platform == b'O') * weights))
