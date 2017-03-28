#!/usr/bin/python

import random
from collections import defaultdict

numRaces = 0

# Create a list of names to use as dictionary keys
fh = open('horses.txt')
lines = fh.readlines()
names = [line.rstrip() for line in lines]

# Generate times for horses (no 2 horses are alike) with 2-digit times (for easy printing)
times = [random.choice([i for i in xrange(10, 99)]) for r in xrange(len(names))]

# Initate the dictionaries
horseTimes = dict(zip(names, times))
scoreboard = defaultdict(dict)

def updateScoreboard() :
	for horse in names :
	 	for relation in scoreboard[horse].copy() :
			inceptions = zip(scoreboard[relation].keys(), scoreboard[relation].values())
			for inception in inceptions :
				if scoreboard[horse][relation] == inception[1] :
					scoreboard[horse][inception[0]] = inception[1]

def getNumRelations() :
	numRelations = 0
	for horse in scoreboard :
		numRelations += len(scoreboard[horse])
	return numRelations

# Horrible hack for creating a heats of 5, where the last horse in each heat also competes in the next one
heats = [[names[i] for i in range(j, j+5)] for j in range(0,len(names)-4,4)] #FIXME superflous horses glued!

# Qualifying races!
for heat in heats :
	race = zip([horseTimes[heat[i]] for i in range(0, len(heat))], heat)
	race.sort()
 	numRaces += 1

	# Create the first entries in the scoreboard
	for position in range(5) :
		for faster in range(0, position) :
			scoreboard[race[position][1]][race[faster][1]] = True
		for slower in range(position+1, 5) :
			scoreboard[race[position][1]][race[slower][1]] = False

print(getNumRelations())

# We now have a starting point where each horse has 4 or 8 relations
# (the horses that ran in two heats have twice the relations)
#
# Go through the scoreboard and try to build additional relations
updateScoreboard()
updateScoreboard() # with the updated scoreboard run it again for even more relations (third time is not the charm, twice is enough!)

#while len(names) * len(names) < getNumRelations() : # the scoreboard is not complete, need to run more races 
	

print(numRaces)
