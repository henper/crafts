import numpy as np

left = [
3,
4,
2,
1,
3,
3,
]

right = [
4,
3,
5,
3,
9,
3,
]

from input import right, left

right.sort()
left.sort()

right = np.array(right)
left  = np.array(left)

diff = right - left

print(sum(np.abs(diff)))
