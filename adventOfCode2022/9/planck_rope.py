import numpy as np

head = np.array([0, 0])
tail = np.array([0, 0])

history_of_the_tail = np.array([tail])

with open('./adventOfCode2022/9/input.txt', 'r') as input:
    for line in input:
        direction, distance = line.split()

        match direction:
            case 'U':
                delta_dir = np.array([ 0,  1])
            case 'D':
                delta_dir = np.array([ 0, -1])
            case 'R':
                delta_dir = np.array([ 1,  0])
            case 'L':
                delta_dir = np.array([-1,  0])

        for step in range(1, 1+int(distance)):
            head += delta_dir

            # not adjacent if any coordinate distance is 2
            if np.any(2 == abs(head - tail)):

                # tail should move towards head
                move = head - tail

                # but only by one step in either direction
                # find the coordinate, x or y, that is two steps away
                c = np.where(2 == abs(head-tail))[0][0]
                move[c] /= 2 # and make it one

                tail += move

                history_of_the_tail = np.concatenate((history_of_the_tail, [tail]))

    print(np.unique(history_of_the_tail, axis=0).shape[0])
