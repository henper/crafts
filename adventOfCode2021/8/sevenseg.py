import re

prog = re.compile('([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) \| ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+)')

f = open("adventOfCode2021/8/input.txt", 'r')

sum = 0

for line in f:
    result = prog.match(line)

    uniquePatterns = []
    for i in range(1,11):
        uniquePatterns.append(set(result.group(i)))
    uniquePatterns = sorted(uniquePatterns, key=len)

    '''
    0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

    5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
    '''

    one = uniquePatterns[0]
    two = {}
    three = {}
    four = uniquePatterns[2]
    five = {}
    six = {}
    seven = uniquePatterns[1]
    eight = uniquePatterns[9]
    nine = {}

    # find the 6 and c segment by comparing 7 to 0, 6 and 9
    for i in range(6, 9):
        if len(seven.difference(uniquePatterns[i])) == 1:
            six = uniquePatterns[i]

            # now find the 0 and 9 by comparing 4 with 0 and 9
            j,k = set(range(6,9)).difference(set([i]))
            if len(four.difference(uniquePatterns[j])) == 1:
                zero = uniquePatterns[j]
                nine = uniquePatterns[k]
            else:
                zero = uniquePatterns[k]
                nine = uniquePatterns[j]
            break

    # find the 3 by comparing with 1
    for i in range(3, 6):
        if len(one.difference(uniquePatterns[i])) == 0:
            three = uniquePatterns[i]

            # now find the 2 and 5 by comparing with 6
            j,k = set(range(3,6)).difference(set([i]))
            if len(uniquePatterns[j].difference(six)) == 0:
                five = uniquePatterns[j]
                two = uniquePatterns[k]
            else:
                five = uniquePatterns[k]
                two = uniquePatterns[j]
            
    # all numbers found, now figure out what the display says
    translation = [zero, one, two, three, four, five, six, seven, eight, nine]
    gibberish = [set(result.group(11)), set(result.group(12)), set(result.group(13)), set(result.group(14))]

    n = 0
    n += translation.index(gibberish[0]) * 1000
    n += translation.index(gibberish[1]) * 100
    n += translation.index(gibberish[2]) * 10
    n += translation.index(gibberish[3]) * 1

    sum += n

print(sum)


'''
    nbrs = [result.group(11), result.group(12), result.group(13), result.group(14)]

    for nbr in nbrs:
        if len(nbr) == 2:
            ones += 1
        if len(nbr) == 3:
            sevens += 1
        if len(nbr) == 4:
            fours += 1
        if len(nbr) == 7:
            eigths += 1

print(f'ones : {ones}')
print(f'fours : {fours}')
print(f'sevens : {sevens}')
print(f'eigths : {eigths}')
'''