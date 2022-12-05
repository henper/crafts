import re

def range2set(elf: str):
    begin, end = elf.split('-')
    return set(range(int(begin), int(end)+1))

with open('./adventOfCode2022/4/input.txt', 'r') as cleaners:
    redundancies = 0
    overlaps = 0

    for line in cleaners:
        elf_a, elf_b = line.split(',')

        elf_a = range2set(elf_a)
        elf_b = range2set(elf_b)

        if elf_a.issubset(elf_b) or elf_a.issuperset(elf_b):
            redundancies += 1

        if elf_a.intersection(elf_b):
            overlaps += 1

    print(redundancies)
    print(overlaps)
