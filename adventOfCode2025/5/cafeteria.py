from input import ranges, ids


fresh = 0
for id in ids:
    for r in ranges:
        if id >= r.start and id <= r.stop:
            fresh += 1
            break

print(f"Fresh IDs: {fresh}")
