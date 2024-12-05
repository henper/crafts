
rules = [
    (47,53),
    (97,13),
    (97,61),
    (97,47),
    (75,29),
    (61,13),
    (75,53),
    (29,13),
    (97,29),
    (53,29),
    (61,53),
    (97,53),
    (61,29),
    (47,13),
    (75,47),
    (97,75),
    (47,61),
    (75,61),
    (47,29),
    (75,13),
    (53,13),
]

updates = [
    [75,47,61,53,29],
    [97,61,53,29,13],
    [75,29,13],
    [75,97,47,61,53],
    [61,13,29],
    [97,13,75,29,47],
]

from input import rules, updates
ordered = []
reordered = []

def is_rule_follower(update, applicable_rules):
    for i, page in enumerate(update):
        # check if this page needs to be after any of the following pages
        for rule in applicable_rules:
            if page == rule[1] and rule[0] in update[i:]:
                return False
    return True

def rule_breaker_breaker(update, applicable_rules):

    # Flip all rule breakers
    while True:
        flipped = False

        # Find a rule breaker
        for i, page in enumerate(update):
            # check if this page needs to be after any of the following pages
            for rule in applicable_rules:
                if page == rule[1] and rule[0] in update[i:]:

                    j = i + update[i:].index(rule[0])

                    update[i], update[j] = update[j], update[i]

                    flipped = True
                    break

            if flipped:
                break

        if is_rule_follower(update, applicable_rules):
            break

    reordered.append(update)

for update in updates:

    filtered_rules = list(filter(lambda rule: rule[0] in update or rule[1] in update, rules))

    if is_rule_follower(update, filtered_rules):
        ordered.append(update)
    else:
        rule_breaker_breaker(update, filtered_rules)


creamy_centers = [update[len(update)//2] for update in ordered]
print(sum(creamy_centers))

creamy_centers = [update[len(update)//2] for update in reordered]
print(sum(creamy_centers))

