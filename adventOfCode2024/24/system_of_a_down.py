from operator import xor  as XOR, and_ as AND, or_ as OR

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

def getval(wire):
    if type(system[wire]) is tuple:
        w1, op, w2 = system[wire]
        return op(getval(w1), getval(w2))
    else:
        return system[wire]

# find the outputs
outputs = list(filter(lambda key: 'z' in key, system.keys()))
outputs.sort()
outputs.reverse()

register = ''
for output in outputs:
    val = getval(output)
    register += '1' if val else '0'

print(int(register, 2))
