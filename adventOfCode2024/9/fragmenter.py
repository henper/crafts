
disk_map = '2333133121414131402'

from input import disk_map

file_sizes = disk_map[::2]
free_space = disk_map[1::2]


# Generate disk representation
unified = []
files = [] # Create list without the empty spaces, such that we have a list that we can pick file blocks from
for i in range(len(file_sizes)):
    file = [i] * int(file_sizes[i])
    files += file
    unified += file

    if i < len(free_space):
        unified += '.' * int(free_space[i])

#print(unified)

fragmented = []
space = 0
prev = 0
while len(fragmented) < len(files):
    next = prev + unified[prev:].index('.')

    # add any files that are already in place
    fragmented += unified[prev:next]

    # pick file block from the end of the file list, and put them in the empty spaces
    fragmented += [files[-space-1]]

    space += 1
    prev = next + 1

# strip surplus
fragmented = fragmented[:len(files)]

#print(fragmented)

def checksum(fragmented):
    sum = 0
    for i in range(len(fragmented)):
        if fragmented[i] == '.':
            break
        sum += i * int(fragmented[i])
    return sum

print(checksum(fragmented))


'009981118882777333644655556666667775'
'00998111888277733364465555666666'
'0099811188827773336446555566'
'0099811188827773336446555566'