from input import *

start = 'AAA'
goal  = 'ZZZ'

steps = 0

class Ghost_walker():

    def __init__(self):
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


ghost = Ghost_walker()

steps = 0
while (ghost.position is not goal):
    ghost.step()
    steps += 1




print(steps)
