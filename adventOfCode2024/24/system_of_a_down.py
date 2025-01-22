from operator import xor  as XOR, and_ as AND, or_ as OR

system = {
    'x00': 0,
    'x01': 1,
    'x02': 0,
    'x03': 1,
    'x04': 0,
    'x05': 1,
    'y00': 0,
    'y01': 0,
    'y02': 1,
    'y03': 1,
    'y04': 0,
    'y05': 1,

   'z05': ('x00', AND, 'y00'),
   'z02': ('x01', AND, 'y01'),
   'z01': ('x02', AND, 'y02'),
   'z03': ('x03', AND, 'y03'),
   'z04': ('x04', AND, 'y04'),
   'z00': ('x05', AND, 'y05'),
}

system = {
    'x00': True,
    'x01': False,
    'x02': True,
    'x03': True,
    'x04': False,
    'y00': True,
    'y01': True,
    'y02': True,
    'y03': True,
    'y04': True,

    'mjb': ('ntg', XOR, 'fgs'),
    'tnw': ('y02', OR , 'x01'),
    'z05': ('kwq', OR , 'kpj'),
    'fst': ('x00', OR , 'x03'),
    'z01': ('tgd', XOR, 'rvg'),
    'bfw': ('vdt', OR , 'tnw'),
    'z10': ('bfw', AND, 'frj'),
    'bqk': ('ffh', OR , 'nrd'),
    'djm': ('y00', AND, 'y03'),
    'psh': ('y03', OR , 'y00'),
    'z08': ('bqk', OR , 'frj'),
    'frj': ('tnw', OR , 'fst'),
    'z11': ('gnj', AND, 'tgd'),
    'z00': ('bfw', XOR, 'mjb'),
    'vdt': ('x03', OR , 'x00'),
    'z02': ('gnj', AND, 'wpb'),
    'kjc': ('x04', AND, 'y00'),
    'qhw': ('djm', OR , 'pbm'),
    'hwm': ('nrd', AND, 'vdt'),
    'rvg': ('kjc', AND, 'fst'),
    'fgs': ('y04', OR , 'y02'),
    'pbm': ('y01', AND, 'x02'),
    'kwq': ('ntg', OR , 'kjc'),
    'tgd': ('psh', XOR, 'fgs'),
    'z09': ('qhw', XOR, 'tgd'),
    'kpj': ('pbm', OR , 'djm'),
    'ffh': ('x03', XOR, 'y03'),
    'ntg': ('x00', XOR, 'y04'),
    'z06': ('bfw', OR , 'bqk'),
    'wpb': ('nrd', XOR, 'fgs'),
    'z04': ('frj', XOR, 'qhw'),
    'z07': ('bqk', OR , 'frj'),
    'nrd': ('y03', OR , 'x01'),
    'z03': ('hwm', AND, 'bqk'),
    'z12': ('tgd', XOR, 'rvg'),
    'gnj': ('tnw', OR , 'pbm'),  
}

from input import system

def evaluate(wire, network: set):
    if type(system[wire]) is tuple:
        w1, op, w2 = system[wire]
        network.update((w1, w2))
        return op(evaluate(w1, network), evaluate(w2, network))
    else:
        return system[wire]

def coalesce(l):
    ls = list(filter(lambda key: l in key, system.keys()))
    ls.sort()
    ls.reverse()
    return ls


def register(ls):
    r = ''
    networks = []
    for l in ls:
        network = set()
        val = evaluate(l, network)
        r += '1' if val else '0'
        networks.append(network)
    return int(r, 2), networks


x,_ = register(coalesce('x'))
y,_ = register(coalesce('y'))
z,n = register(coalesce('z'))

gates = list(filter(lambda key: type(system[key]) is tuple, system))
original = system.copy()

# z35, index 10 only depends on two inputs -y35 and x35. This means we can split the problem in twain.

'''
Go from least to most significant bit, and ensure the addition adds up. If not, then switch gates til it does.
'''

for i in range(len(n)):

    bitmask = int('1' * (i+1), 2)
    carry   = int('1' * (i+2), 2)

    xb = x & bitmask
    yb = y & bitmask

    zb = z & carry

    if xb + yb != zb:
        pass

    pass

'''
Brute force search
'''

from itertools import combinations

gate_swaps = combinations(gates, 2)
swaps = combinations(gate_swaps, 4)

for swap in swaps:

    # disqualify swaps where the same gate appears more than once
    A,B = zip(*swap)

    if len(set(A+B)) < 8:
        continue

    system = original.copy()
    for gate_swap in swap:
        a, b = gate_swap

        system[a], system[b] = system[b], system[a] 

    z = register(coalesce('z'))

    if x + y == z:
    #if x & y == z:
        S = list(A+B)
        S.sort()
        print(','.join(S))
        break





