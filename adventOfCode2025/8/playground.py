from pygame.math import Vector3
from collections import OrderedDict

from example import junction_boxes

distances = {}

for box_idx, box in enumerate(junction_boxes[:-1]):
    for neighbor in junction_boxes[box_idx+1:]:
        key = [box, neighbor]
        key.sort(key=lambda x: Vector3(x).magnitude())
        key = (key[0], key[1])
        if key in distances:
            continue
        distances[key] = Vector3(box).distance_to(Vector3(neighbor))

print(len(distances))

# Sort by distance
distances = OrderedDict(sorted(distances.items(), key=lambda item: item[1]))

# Create circuits from the 10 shortest distances
connections = 0
circuits = []
for key in list(distances.keys()):
    box_a, box_b = key

    print(f"Connecting {box_a} to {box_b} with distance {distances[key]}")

    if connections >= 10:
        break

    appended = False
    circuit_idx = None
    pop_list = []
    for idx, circuit in enumerate(circuits):
        if box_a in circuit and box_b in circuit:
            appended = True
            connections += 1
            break
        elif box_a in circuit and not appended:
            appended = True
            circuit_idx = idx
            connections += 1
            circuit.add(box_b)
        elif box_b in circuit and not appended:
            circuit.add(box_a)
            circuit_idx = idx
            connections += 1
        elif appended and box_a in circuit or box_b in circuit:
            circuits[circuit_idx] = circuits[circuit_idx].union(circuit)
            pop_list.append(idx)
            break

    for idx in sorted(pop_list, reverse=True):
        circuits.pop(idx)

    if not appended:
        circuits.append(set([box_a, box_b]))
        connections += 1

print(f"Total circuits: {len(circuits)}")
for idx, circuit in enumerate(circuits):
    print(f"Circuit {idx+1}: {circuit}")
