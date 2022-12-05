
'''
stacks = [['N', 'Z'], ['D','C','M'], ['P']]

'''
stacks = [
['R',
 'Q',
 'G',
 'P',
 'C',
 'F'],

['P',
 'C',
 'T',
 'W'],

['C',
 'M',
 'P',
 'H',
 'B'],

['R',
 'P',
 'M',
 'S',
 'Q',
 'T',
 'L'],

['N',
 'G',
 'V',
 'Z',
 'J',
 'H',
 'P'],

['J',
 'P',
 'D'],

['R',
 'T',
 'J',
 'F',
 'Z',
 'P',
 'G',
 'L'],

['J',
 'T',
 'P',
 'F',
 'C',
 'H',
 'L',
 'N'],

['W',
 'C',
 'T',
 'H',
 'Q',
 'Z',
 'V',
 'G']
]


with open('./adventOfCode2022/5/input.txt', 'r') as arrangements:
    for arrangement in arrangements:
        no = int(arrangement.split()[1])
        fo = int(arrangement.split()[3]) - 1
        to = int(arrangement.split()[5]) - 1

        flip = stacks[fo][:no]
        #flip.reverse()

        stacks[fo] = stacks[fo][no:]
        stacks[to] = flip + stacks[to]


for stack in stacks:
    print(stack[0], end='')
