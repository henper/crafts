from input import hot_springs

permutations = 0

def traverse_group(springs, records, count, d):
    global permutations

    # If we've counted the amount of damaged springs that the record show, the next spring must be operational
    # if it's not then this branch did not yield a valid permutation
    # if it is, then we should continue with the next record
    if count == records[0]:
        if springs and springs[0] == '#':
            return 0
        else:
            if len(records) == 1:
                # that was the last record, now we just need to determine if this was a successful permutation
                if springs and '#' in springs:
                    return # we've failed to count some of the actually damaged springs, meaning some operational springs were mis-labeled

                permutations += 1
                if springs:
                    d += '.' * len(springs)
                print(d)
                return

            # continue in the same branch
            d = d + '.'
            springs = springs[1:]
            count = 0
            records.pop(0)

    if not springs:
        return

    # If we've started counting, there are not any new possibilities. Any encountered spring must be damaged
    # it it's not then this branch did not yield a valid permutation
    if springs[0] == '.':
        if count:
            return
        # not yet started counting, operational springs should not be counted
        return traverse_group(springs[1:], records, count, d + '.')

    # If we have yet to start counting damaged springs
    # and the next spring is an unknown, that leaves us with two possibilities
    if count == 0 and springs[0] == '?':
        traverse_group(springs[1:], records.copy(), count + 1, d + '#') # damaged
        traverse_group(springs[1:], records.copy(), count + 0, d + '.') # operational
        return

    # At this point we're at a damaged spring, known or unknown, and should count it
    return traverse_group(springs[1:], records, count + 1, d + '#')






for row in hot_springs:
    line, records = row
    records = list(records)

    traverse_group(line, records, 0, '')

    print(permutations)
    #permutations = 0
