from example import workflows, parts
import re


import operator
do = {'<': operator.lt, '>': operator.gt}


def deconstruct_rule(rule):
    m = re.search('(?P<affix>\w)(?P<operand>[<|>])(?P<value>\d+):(?P<next>\w+)', rule)
    return m.group('affix'), m.group('operand'), int(m.group('value')), m.group('next')

# Reduce the workflows by identifying all paths that lead to Accepted

# Since we're building a list of rules that must all be false for the path to Accepted to succeed,
# some rules need to be reversed, i.e. rules that leads to Accepted with condition or to
# another workflow that leads to Accepted.
def reverse_rule(affix, operand, value):
    reversed_rule  = affix
    reversed_rule += '>' if operand == '<' else '<'
    value += 1 if operand == '>' else -1
    reversed_rule += str(value)
    reversed_rule += ':R'
    return reversed_rule

def find_workflow_with_rule_to_other(other) -> (str, list):
    for key, rules in workflows.items():
        for rule in rules:
            if rule == other:
                return (key, rules[:rules.index(rule)])
            if len(rule) <= 3:
                continue

            affix, operand, value, next = deconstruct_rule(rule)
            if next == other:
                rules = rules[:rules.index(rule)]
                rules.append(reverse_rule(affix, operand, value))
                return (key, rules)

    return (None, None)

def traverse_workflow_rules(workflow, rules, compound_rules):
    compound_rules += rules
    workflow, rules = find_workflow_with_rule_to_other(workflow)

    if workflow is not None:
        traverse_workflow_rules(workflow, rules, compound_rules)
    return


paths_to_accepted = []
for key, rules in workflows.items():
    for rule in rules:
        if rule == 'A':
            paths_to_accepted.append([])
            traverse_workflow_rules(key, rules[:-1], paths_to_accepted[-1])
            continue
        if rule[-1] == 'A':
            affix, operand, value, next = deconstruct_rule(rule)
            modded_rules = rules[:rules.index(rule)]
            modded_rules.append(reverse_rule(affix, operand, value))

            paths_to_accepted.append([])
            traverse_workflow_rules(key, modded_rules, paths_to_accepted[-1])


def accepted(part, path):
    for rule in path:
        affix, operand, value, _ = deconstruct_rule(rule)
        if do[operand](part[affix], value):
            return False # not Accepted by this path (as all rules in the path must be false)
    return True

# Recreate part 1 for kicks (and to verify that the logic works)
answer = 0
for part in parts:
    for path in paths_to_accepted:
        if accepted(part, path):
            answer += part['x'] + part['m'] + part['a'] + part['s']
            break
print(answer)

# Now begin with xmas full-ranges (oh, no. Not Day 5 again) and reduce them for every path
# to get all combinations that is accepted by every path
accepted_ranges = []
for path in paths_to_accepted:
    accepted_range = { 'x': [1,4000], 'm': [1,4000], 'a': [1,4000],  's': [1,4000] }

    for rule in path:
        affix, operand, value, _ = deconstruct_rule(rule)
        if operand == '<' and value > accepted_range[affix][0]:
            accepted_range[affix][0] = value
        elif operand == '>' and value < accepted_range[affix][1]:
            accepted_range[affix][1] = value


    accepted_ranges.append(accepted_range)

# Remove overlap from accepted ranges
# TODO how..

answer = 0
for accepted_range in accepted_ranges:
    combinations = 1
    for affix in ['x', 'm', 'a', 's']:
        combinations *= 1 + accepted_range[affix][1] - accepted_range[affix][0]
    answer += combinations
print(answer)

# Add workflows for accepted and rejected with corresponding rules
workflows['A'] = ['A']
workflows['R'] = ['R']


def is_accepted(part, workflow):
    for rule in workflow:
        # Perform simple rules, Accepted, Rejected or next workflow without conditions
        if len(rule) <= 3:
            if rule == 'A':
                return True
            if rule == 'R':
                return False
            return is_accepted(part, workflows[rule])

        # Deconstruct complicated rule and see if it is applicable
        affix, operand, value, next = deconstruct_rule(rule)

        if do[operand](part[affix], value):
            return is_accepted(part, workflows[next])


answer = 0
for part in parts:
    if is_accepted(part, workflows['in']):
        answer += part['x'] + part['m'] + part['a'] + part['s']
print(answer)

