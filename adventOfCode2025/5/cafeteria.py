from input import ranges, ids

'''
fresh = 0
for id in ids:
    for r in ranges:
        if id >= r.start and id <= r.stop:
            fresh += 1
            break

print(f"Fresh IDs: {fresh}")
'''

def reduce(ranges):
    reduced = []

    for r in ranges:
        handled = False
        for rr in reduced.copy():
            # Fully contained
            if r.start >= rr.start and r.stop <= rr.stop:
                handled = True
                break # drop

            # Fully encompasses
            if r.start <= rr.start and r.stop >= rr.stop:
                reduced.remove(rr) # replace
                reduced.append(r)
                handled = True
                break

            # Overlaps left
            if r.start <= rr.start and r.stop >= rr.start:
                reduced.remove(rr)
                reduced.append(range(r.start, rr.stop))
                handled = True
                break

            # Overlaps right
            if r.start <= rr.stop and r.stop >= rr.stop:
                reduced.remove(rr)
                reduced.append(range(rr.start, r.stop))
                handled = True
                break

            # Adjacent left
            if r.stop + 1 == rr.start:
                reduced.remove(rr)
                reduced.append(range(r.start, rr.stop))
                handled = True
                break

            # Adjacent right
            if r.start - 1 == rr.stop:
                reduced.remove(rr)
                reduced.append(range(rr.start, r.stop))
                handled = True
                break

        if not handled:
            reduced.append(r)

    return reduced

reduced = reduce(ranges)

while len(reduced) != len(ranges):
    ranges = reduced
    reduced = reduce(ranges)

print(f'ranges: {len(ranges)} reduced: {len(reduced)}')

sum_fresh_ids = 0
for r in reduced:
    sum_fresh_ids += len(r) + 1

print(f"Fresh IDs: {sum_fresh_ids}")

# reduced to 85, fresh ids 338189277144468, too low

# reduced to 78, fresh ids 338189277144471, too low
