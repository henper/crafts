import re


translation = {}
numbers = "0123456789"
for number in numbers:
    translation[number] = '.'

symbols = "!\"#¤%&/()=?@£${[]}\\+-_"
for symbol in symbols:
    translation[symbol] = 'S'

translation = str.maketrans(translation)


schematic = open('./adventOfCode2023/3/input.txt', 'r').readlines()
num_lines = len(schematic)
line_len  = len(schematic[0])

actual_part_nos = []
for line_num, line in enumerate(schematic):

    # Find a number and it's position
    end = 0

    part_nos = re.findall('([0-9]+)', line[end+1:])

    for part_no in part_nos:
        start = end + line[end:].index(part_no)
        end   = start + len(part_no)

        # determine if this is an actual part number
        frame = ''
        frame = frame + schematic[line_num-1][start-1:end+1]
        frame = frame + schematic[line_num][start-1] + schematic[line_num][end]
        frame = frame + schematic[line_num+1][start-1:end+1]
        #frame = frame + schematic[line_num+1][start-1:end+1]

        #frame = frame.translate(translation) # replace all numbers with dots
        if len(frame) * '.' != frame:        # compare the frame with a string of the same length filled with all dots
            actual_part_nos.append(int(part_no))


print(sum(actual_part_nos))
