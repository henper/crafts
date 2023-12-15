from input import sequence
from collections import OrderedDict

def hash(instruction: str):
    val = 0
    for char in instruction:
        val += ord(char)
        val *= 17
        val %= 256

    return val


boxes = [OrderedDict() for i in range(256)]

for instruction in sequence:
    # split the instruction into label, operation and possibly focal strength
    addition = instruction.split('=')
    if len(addition) == 2:
        label, focal = addition
        boxes[hash(label)][label] = int(focal)
    else:
        label = instruction.split('-')[0]
        boxnum = hash(label)
        if label in boxes[boxnum].keys():
            boxes[boxnum].pop(label)


answer = 0
for i, box in enumerate(boxes):

    if len(box) == 0:
        continue

    for slot, (label, focal) in enumerate(box.items()):
        answer += (i+1) * (slot+1) * focal

print(answer)




