import re

multiplications = []

with open('input.txt') as instructions:
    for instruction in instructions:

        matches = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', instruction)

        for match in matches:
            operands = re.findall('\d+', match)
            operands = [ int(o) for o in operands]
            multiplications.append(operands[0] * operands[1])

print(sum(multiplications))
