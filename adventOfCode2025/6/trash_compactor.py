import pandas as pd
import numpy as np

from functools import reduce
from operator import mul, add

pd.options.display.max_colwidth = None

df = pd.read_csv('adventOfCode2025/6/input.txt', header=None)

# Extract and remove the operators from the last row
ops = df.iloc[-1].to_string(index=False, ).split()
df = df.drop(index=df.shape[0]-1)

# Convert rows of strings to rows with each character in its own column
df = df[0].apply(lambda x: pd.Series(list(str(x))))
df = df.fillna(' ')

# Go through all columns and calculate the answers
answers = []
numbers = []
problem = 0
space_series = pd.Series([' '] * df.shape[0])
for col in df.columns:
    # when hitting a column of all spaces, sum/prod all numbers and then advance to the next problem
    if space_series.compare(df[col]).empty:

        if ops[problem] == '+':
            answers.append(reduce(add, numbers))
        elif ops[problem] == '*':
            answers.append(reduce(mul, numbers))

        problem += 1
        numbers.clear()
        continue

    numbers.append(int(df[col].to_string(index=False, header=False).translate(str.maketrans('', '', ' \n'))))

# last set of numbers are not followed by an empty column so do the last problem here
if ops[problem] == '+':
    answers.append(reduce(add, numbers))
elif ops[problem] == '*':
    answers.append(reduce(mul, numbers))

print(f'sum total: {reduce(add, answers)}')
