import pandas as pd
import numpy as np

from functools import reduce
from operator import mul, add

df = pd.read_csv('adventOfCode2025/6/input.csv', header=None)

answers = []
for col in df.columns:
    l = list(df[col])
    n = [int(n) for n in l[:-1]]
    op = l[-1]

    if op == '+':
        answers.append(reduce(add, n))
    elif op == '*':
        answers.append(reduce(mul, n))

print(f'sum total: {reduce(add, answers)}')
