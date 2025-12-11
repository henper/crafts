from itertools import combinations_with_replacement
from numpy import array, all, any

from example import machines

answer = 0

# part 1
for machine in machines:
    indicators, buttons, _ = machine

    indicators = [i=='#' for i in list(indicators)]
    result = [False] * len(indicators) # all off would mean that no clicks are needed

    clicks = 0

    while result != indicators:
        clicks += 1

        clicked_combos = combinations_with_replacement(buttons, clicks)
        #clicked_combos = list(clicked_combos) # comment me!
        for clicked in clicked_combos:

            for click in clicked:
                if type(click) == int:
                    click = (click,)
                for activation in click:
                    result[activation] ^= True

            if result == indicators:
                break

            result = [False] * len(indicators)

    answer += clicks
    #print(clicks)
    #print(clicked)

print(answer)

answer = 0
# part 2
for machine in machines:
    _, buttons, joltage_requirements = machine

    result = [0] * len(joltage_requirements) # no joltage requirements would mean that no clicks are needed

    result = array(result)
    joltage_requirements = array(joltage_requirements)
    diff = joltage_requirements - result

    new_cache = {(): result} # no click results in no joltages


    clicks = 0
    while any(diff != 0):
        cache = new_cache
        new_cache = {}

        print(f"cache length: {len(cache)}")

        clicks += 1
        clicked_combos = combinations_with_replacement(buttons, clicks)
        clicked_combos = list(clicked_combos) # comment me!
        for clicked in clicked_combos:

            # fetch the result from the previously built cache
            try:
                result = cache[clicked[:-1]].copy()
            except KeyError:
                continue # this combo of clicks have exceeded the requirements

            click = clicked[-1]
            if type(click) == int:
                click = (click,)
            for activation in click:
                result[activation] += 1

            # store the result of the clicks in the cache for the next number of clicks
            diff = joltage_requirements - result
            if all(diff >= 0):
                new_cache[clicked] = result

            if all(diff == 0):
                break


    answer += clicks
    print(clicks)
    #print(clicked)

print(f'answer: {answer}')
