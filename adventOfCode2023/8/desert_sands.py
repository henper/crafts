from input import *

start = 'AAA'
goal  = 'ZZZ'

position = start
dir_pos  = -1
steps = 0

while (position is not goal):
    steps += 1

    dir_pos += 1
    if (dir_pos >= len(directions)):
        dir_pos = 0

    dir = directions[dir_pos]

    if (dir == 'L'):
        position,_ = map[position]
    else:
        _,position = map[position]

print(steps)
