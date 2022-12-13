"""
add 'packet_pairs = [' and closing ']' to top and bottom of input
search replace ']\n' with '],\n' and '\n^' with '], [\n'
"""
#from example import packet_pairs
from input import packet_pairs

from functools import cmp_to_key

def compare(a, b):
    # compare integers
    if type(a) is int and type(b) is int:
        return b - a

    # convert mixed types
    if type(a) is list and type(b) is not list:
        b = [b]

    if type(a) is not list and type(b) is list:
        a = [a]

    # compare lists
    for i in range(max(len(a), len(b))):
        if i >= len(a):
            return 1  # left side ran out of items (ordered)

        if i >= len(b):
            return -1 # right side ran out of items (out-of-order)

        res = compare(a[i], b[i])
        if res == 0:
            continue
        return res

    return 0


pix = 0
ordered_indicies = []

for a, b in packet_pairs:
    pix += 1
    if compare(a, b) > 0:
        ordered_indicies.append(pix)

# step 1
print(sum(ordered_indicies))

packets = [[[2]], [[6]]]
for a, b in packet_pairs:
    packets.append(a)
    packets.append(b)


packets.sort(key=cmp_to_key(compare), reverse=True)

pix = 0
divider_packet_indices = []
for packet in packets:
    pix += 1
    if packet == [[2]] or packet == [[6]]:
        divider_packet_indices.append(pix)

# step 2
print(divider_packet_indices[0] * divider_packet_indices[1])
