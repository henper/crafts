from input import *
import timeit


class Ghost_walker():

    def __init__(self, start):
        self.position = start
        self.dir_pos  = -1

    def step(self):
        self.dir_pos += 1
        if (self.dir_pos >= len(directions)):
            self.dir_pos = 0

        dir = directions[self.dir_pos]

        if (dir == 'L'):
            self.position,_ = map[self.position]
        else:
            _,self.position = map[self.position]

        if self.position[2] == 'Z':
            return True
        else:
            return False


# Find start position and create ghosts
ghosts = []
for key in map.keys():
    if key[2] == 'A':
        ghosts.append(Ghost_walker(key))

print(f'ghosts: {len(ghosts)}')

steps = 0



while(True):
    all_done = True
    steps += 1

    start = timeit.default_timer()


    for ghost in ghosts:

        if not ghost.step():
            # should continue
            all_done = False

    if (steps % 1000000 == 0):
        end = timeit.default_timer()
        print(f'start: {start}')
        print(f'end: {end}')
        print('1M step time: {}'.format(end-start))
        start = end

    if all_done:
        break





print(steps)
