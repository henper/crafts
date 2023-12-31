from input import workflows, parts
import re

# Add workflows for accepted and rejected with corresponding rules
workflows['A'] = ['A']
workflows['R'] = ['R']

import operator
do = {'<': operator.lt, '>': operator.gt}

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
        m = re.search('(?P<affix>\w)(?P<operand>[<|>])(?P<value>\d+):(?P<next>\w+)', rule)
        affix   = m.group('affix')
        operand = m.group('operand')
        value   = m.group('value')
        next    = m.group('next')

        if do[operand](part[affix], int(value)):
            return is_accepted(part, workflows[next])


answer = 0
for part in parts:
    if is_accepted(part, workflows['in']):
        answer += part['x'] + part['m'] + part['a'] + part['s']

print(answer)