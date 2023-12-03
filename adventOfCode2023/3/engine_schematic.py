import re

schematic = open('./adventOfCode2023/3/input.txt', 'r').readlines()

def num_len(str):
    m = re.search('^([0-9]+)', str)
    if (m):
        return len(m.group(1))
    else:
        return 1

gear_ratios = []
for line_num, line in enumerate(schematic):

    # Find a number and it's position
    end = 0

    gears = re.findall('\*', line[end+1:])

    for gear in gears:
        start = end + line[end:].index('*')
        end   = start + 1

        frame = ''

        # expand the frame with any numbers found in the corners and edges
        start_offset = num_len(schematic[line_num-1][start-1::-1]) #top left, backwards
        end_offset   = num_len(schematic[line_num-1][end:]) #top right
        frame = frame + schematic[line_num-1][start-start_offset:end+end_offset]
        frame = frame + '.'
        start_offset = num_len(schematic[line_num][start-1::-1]) #middle left, backwards
        end_offset   = num_len(schematic[line_num][end:]) #middle right
        frame = frame + schematic[line_num][start-start_offset:start] + schematic[line_num][end:end+end_offset]
        frame = frame + '.'
        start_offset = num_len(schematic[line_num+1][start-1::-1]) #bottom left, backwards
        end_offset   = num_len(schematic[line_num+1][end:]) #bottom right
        frame = frame + schematic[line_num+1][start-start_offset:end+end_offset]

        part_nos = re.findall('[0-9]+', frame)
        if (len(part_nos) == 2):
            gear_ratios.append(int(part_nos[0]) * int(part_nos[1]))



print(sum(gear_ratios))
