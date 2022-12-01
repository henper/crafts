import os

elves = [0]

with open('./adventOfCode2022/1/input.txt', 'r') as storage:
    for foodstuff in storage:
        if foodstuff.rstrip():
            elves[-1] = elves[-1] + int(foodstuff)
        else:
            elves.append(0)

elves = sorted(elves)

print(f'top elf: {elves[-1]}')

print(f'top three elves: {elves[-1] + elves[-2] + elves[-3]}')
