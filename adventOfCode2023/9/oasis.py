from input import histories

def extrapolate_underlying_change(progression : list[int]) -> int:

    # Generate the underlying change
    underlying_change = []
    for index, val in enumerate(progression[1:]):
        underlying_change.append(val - progression[index])

    # Check if all zeroes
    if all(0 for c in underlying_change):
        return 0

    return underlying_change[0] - extrapolate_underlying_change(underlying_change)


answer = 0
for history in histories:
    underlying_change = extrapolate_underlying_change(history)
    answer += history[0] - underlying_change

print(answer)
