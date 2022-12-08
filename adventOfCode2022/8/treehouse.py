import numpy as np

# input to matrix
with open('./adventOfCode2022/8/input.txt', 'r') as input:
	trees = []
	for line in input:
		trees.append([int(n) for n in[*line.rstrip()]])

trees = np.array(trees)

# part 1
visible = 0
for y in range(1, trees.shape[0]-1):
	for x in range(1, trees.shape[1]-1):

		tree = trees[y, x]

		# sightlines
		north = trees[ :y   ,  x    ]
		south = trees[  y+1:,  x    ]
		east  = trees[  y   ,  x+1: ]
		west  = trees[  y   , :x    ]

		if np.all(tree > north):
			visible += 1
			continue

		if np.all(tree > south):
			visible += 1
			continue

		if np.all(tree > east):
			visible += 1
			continue

		if np.all(tree > west):
			visible += 1
			continue

print(visible + 2 * sum(trees.shape) - 4)

# part 2
def scenic_score(tree : int, heights : np.array):
	# special case if we're at the edge of the clearing
	if heights.size == 0: return 0

	gteq = tree <= heights

	# special case if there's only one tree and we can see over it
	if len(gteq) == 0 and not gteq:
		return 1

	# select the indices of all trees that are greater or of equal height
	gteq_indices = np.where(gteq)[0]

	# special case if all trees where lower
	if len(gteq_indices) == 0:
		return len(heights)

	return min(gteq_indices) + 1


scores = []
for y in range(trees.shape[0]-1):
	for x in range(trees.shape[1]-1):

		tree = trees[y, x]

		# sightlines
		north = trees[ :y   ,  x    ]
		south = trees[  y+1:,  x    ]
		east  = trees[  y   ,  x+1: ]
		west  = trees[  y   , :x    ]

		north = np.flip(north)
		west  = np.flip(west)

		sightlines = [north, south, east, west]

		scenicity = 1
		for line in sightlines:
			score = scenic_score(tree, line)
			scenicity *= score

		scores.append(scenicity)

print(max(scores))
