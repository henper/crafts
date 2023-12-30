from input import hot_springs

# Cache dictionary
cache = {}

# Manual memoize decorator
def memoize(func):
    def wrapper(springs, records, count, permutations, d):
        hashable = springs + str(records) + str(count) + str(permutations)
        if hashable not in cache:
            cache[hashable] = func(springs, records, count, permutations, d)
        return cache[hashable]

    return wrapper


def traverse_group(springs, records, count, permutations, d):

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
                    return permutations # we've failed to count some of the actually damaged springs, meaning some operational springs were mis-labeled

                if springs:
                    d += '.' * len(springs)
                #print(d, end='\r')
                print(d)
                return permutations + 1

            # continue in the same branch
            d = d + '.'
            springs = springs[1:]
            count = 0
            records.pop(0)

    if not springs:
        return permutations

    # If we've started counting, there are not any new possibilities. Any encountered spring must be damaged
    # it it's not then this branch did not yield a valid permutation
    if springs[0] == '.':
        if count:
            return permutations
        # not yet started counting, operational springs should not be counted
        return traverse_group(springs[1:], records, count, permutations, d + '.')

    # If we have yet to start counting damaged springs
    # and the next spring is an unknown, that leaves us with two possibilities
    if count == 0 and springs[0] == '?':
        perm_branch_a = traverse_group(springs[1:], records.copy(), count + 1, permutations, d + '#') # damaged
        perm_branch_b = traverse_group(springs[1:], records, count + 0, permutations, d + '.') # operational
        return perm_branch_a + perm_branch_b

    # At this point we're at a damaged spring, known or unknown, and should count it
    return traverse_group(springs[1:], records, count + 1, permutations, d + '#')




answer = 0

for row in hot_springs:
    line, records = row
    records = list(records)

    # unfold
    #line = (line + '?') * 5
    #line = line[:-1] # eat the last '?'
    #records = records * 5

    print(line + ' ' + str(records))
    permutations = traverse_group(line, records, 0, 0, '')

    answer += permutations
    print(f'\nPermutations: {permutations}, total: {answer}\n')
