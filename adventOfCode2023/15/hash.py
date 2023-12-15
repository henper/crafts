from input import sequence

def hash(instruction: str):
    val = 0
    for char in instruction:
        val += ord(char)
        val *= 17
        val %= 256

    return val


answer = 0
for instruction in sequence:
    answer += hash(instruction)

print(answer)
