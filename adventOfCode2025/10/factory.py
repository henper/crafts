from itertools import combinations_with_replacement
from numpy import array, all, any, where, count_nonzero

from input import machines

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
    #machine = machines[20]
    _, buttons, joltage_requirements = machine
    print(joltage_requirements)

    result = [0] * len(joltage_requirements) # no joltage requirements would mean that no clicks are needed

    result = array(result)
    joltage_requirements = array(joltage_requirements)
    diff = joltage_requirements - result

    new_cache = {(): result} # no click results in no joltages


    clicks = 0
    while any(diff != 0):
        cache = new_cache
        new_cache = {}

        print(f"[{clicks:2}] cache length: {len(cache)}")

        clicks += 1
        clicked_combos = combinations_with_replacement(buttons, clicks)
        #clicked_combos = list(clicked_combos) # comment me!
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

            diff = joltage_requirements - result

            if all(diff == 0):
                break

            possible = all(diff >= 0) # ensure this combination of clicks have not exceeded any requirement

            # check if two or more joltages are met with the current combination of clicks
            # and then if there is any chance of completing the other requirements with the
            # buttons available
            if possible and len(diff) - count_nonzero(diff) > 0:
                met_indices   = set(where(diff == 0)[0])
                unmet_indices = set(where(diff > 0)[0])
                impossible = []
                for unmet_idx in unmet_indices:
                    impossible.append(True)
                    # see if there is a button that can affect the unmet requirement, without affecting the met ones
                    for button in buttons:
                        if type(button) == int:
                            button = (button,)
                        if unmet_idx not in button:
                            continue
                        if not set(button).intersection(met_indices):
                            impossible[-1] = False
                            break # possible to meet this requirement with this button
                if all(impossible):
                    possible = False

            # store the result of the clicks in the cache for the next number of clicks
            if possible:
                new_cache[clicked] = result



    answer += clicks
    print(f'clicks to solve: {clicks}')
    #print(clicked)
    #break

print(f'answer: {answer}')
