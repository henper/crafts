

with open('./adventOfCode2022/3/input.txt', 'r') as rucksacks:
    prio_sum = 0
    for rucksack in rucksacks:
        compA = set(rucksack.strip()[:len(rucksack)//2])
        compB = set(rucksack.strip()[len(rucksack)//2:len(rucksack)])

        in_both = compA.intersection(compB).pop()

        if in_both.isupper():
            priority = ord(in_both) - 65 + 27
        else:
            priority = ord(in_both) - 96

        prio_sum += priority

    print(prio_sum)

from itertools import zip_longest as izip_longest
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

with open('./adventOfCode2022/3/input.txt', 'r') as rucksacks:
    prio_sum = 0
    for group in grouper(rucksacks, 3, ''):
        badge = set(group[0].strip()).intersection(set(group[1].strip())).intersection(group[2].strip()).pop()

        if badge.isupper():
            priority = ord(badge) - 65 + 27
        else:
            priority = ord(badge) - 96
        prio_sum += priority

    print(prio_sum)
