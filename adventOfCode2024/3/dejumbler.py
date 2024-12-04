import re

multiplications = []

def process_dues(instruction):
    matches = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', instruction)

    for match in matches:
        operands = re.findall('\d+', match)
        operands = [ int(o) for o in operands]
        multiplications.append(operands[0] * operands[1])

def what_to_do(instruction):
    match = re.match("(?P<todo>^.*?)(don't\(\)).*?do\(\)(?P<rest>.*)", instruction)

    if match:
        process_dues(match.group('todo'))
        what_to_do(match.group('rest'))
    else:

        match = re.match("(?P<todo>^.*?)don't\(\)", instruction)
        if match:
            process_dues(match.group('todo'))
        else:
            process_dues(instruction)


with open('example.txt') as instructions:
    for instruction in instructions:
        what_to_do(instruction)


print(sum(multiplications))
