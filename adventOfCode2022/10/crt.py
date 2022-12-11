# totally not stolen from SO
def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

with open('./adventOfCode2022/10/input.txt', 'r') as program:

    pc = 0
    cycle = 0
    #ticks = 20
    ticks = 0

    regx = 1

    sigstr = 0


    while True:

        cycle += 1

        if ticks in range(regx-1, regx+2):
            print('#', end='')
        else:
            print('.', end='')

        ticks += 1
        if (ticks == 40):
            ticks = 0
            strength = cycle * regx
            sigstr += strength
            print('')

        # fetch
        try:
            instruction = peek_line(program).split()[0]
        except IndexError:
            print(sigstr)
            exit()

        # execute
        if instruction == 'noop':
            pc = cycle
            program.readline()

        if instruction == 'addx' and cycle - pc == 2 :
            pc = cycle
            val = int(program.readline().split()[1])
            regx += val
