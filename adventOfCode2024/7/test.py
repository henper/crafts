from itertools import product
from operator import add, mul

def concat(lh: int, rh):
    return int(str(lh) + str(rh))

ops = { '*': mul, '+': add, '||': concat }

tests = {
    190:(10, 19),
    3267:(81, 40, 27),
    83:(17, 5),
    156:(15, 6),
    7290:(6, 8, 6, 15),
    161011:(16, 10, 13),
    192:(17, 8, 14),
    21037:(9, 7, 18, 13),
    292:(11, 6, 16, 20),
}

from input import tests

test_vals = []

for test_val in tests.keys():

    operands = tests[test_val]

    op_combos = product(('+', '*', '||'), repeat=len(operands)-1)

    for op_combo in op_combos:

        lh = operands[0]
        for i in range(len(operands)-1):
            rh = operands[i+1]

            op = ops[op_combo[i]]
            lh = op(lh, rh)

        if lh == test_val:
            test_vals.append(test_val)
            break


print(sum(test_vals))
