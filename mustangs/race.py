#!/usr/bin/python

import random
from collections import defaultdict

# Create a list of names to use as dictionary keys
fh = open('horses.txt')
lines = fh.readlines()
names = [line.rstrip() for line in lines]

# Generate times for horses (no 2 horses are alike) with 2-digit times (for easy printing)
times = [random.choice([i for i in xrange(10, 99)]) for r in xrange(len(names))]

# Initate the dictionaries
horseTimes = dict(zip(names, times))
database = defaultdict(dict)

# Horrible hack for creating a heats of 5, where the last horse in each heat also competes in the next one
heats = [[names[i] for i in range(j, j+5)] for j in range(0,len(names)-4,4)]

# Qualifying races!
for heat in heats :
	race = zip([horseTimes[heat[i]] for i in range(0, len(heat))], heat)
	race.sort()

	# Create the first entries in the database
	for position in range(5) :
		for faster in range(0, position) :
			database[race[position][1]][race[faster][1]] = True
		for slower in range(position+1, 5) :
			database[race[position][1]][race[slower][1]] = False

print(str(database))

