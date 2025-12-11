from itertools import combinations_with_replacement

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
    _, buttons, joltage_requirements = machine

    result = [0] * len(joltage_requirements) # no joltage requirements would mean that no clicks are needed

    clicks = 0

    while result != joltage_requirements:
        clicks += 1

        clicked_combos = combinations_with_replacement(buttons, clicks)
        clicked_combos = list(clicked_combos) # comment me!
        for clicked in clicked_combos:

            for click in clicked:
                if type(click) == int:
                    click = (click,)
                for activation in click:
                    result[activation] += 1

            if result == joltage_requirements:
                break

            result = [0] * len(joltage_requirements)

    answer += clicks
    print(clicks)
    #print(clicked)

print(answer)
