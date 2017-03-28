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

def findUnrelatedHorses( horseList ) :
	unrelated = ['', '' ,'' ,'']
	found = 0;
	for horse in names :
		if horse not in horseList :
			unrelated[found] = horse
			found += 1
			if found == len(unrelated) :
				return unrelated
	#print('short race with only ' + str(found))
	return unrelated[0:found]

def race( heat ) :
	global numRaces
	numRaces += 1
	race = zip([horseTimes[heat[i]] for i in range(0, len(heat))], heat)
	race.sort()
	return zip(*race)[1] # return a sorted tuple of the horses in the race 

def resultToScoreboard( result ) :
	global scoreboard
	for position in range(len(result)) :
		for faster in range(0, position) :
			scoreboard[result[position]][result[faster]] = True
		for slower in range(position+1, len(result)) :
			scoreboard[result[position]][result[slower]] = False

# Horrible hack for creating a heats of 5, where the last horse in each heat also competes in the next one
heats = [[names[i] for i in range(j, j+5)] for j in range(0,len(names)-4,4)] #FIXME superflous horses glued!

# Qualifying races!
for heat in heats :	
	resultToScoreboard(race(heat))

print(getNumRelations())

# We now have a starting point where each horse has 4 or 8 relations
# (the horses that ran in two heats have twice the relations)
#
# Go through the scoreboard and try to build additional relations
updateScoreboard()
updateScoreboard() # with the updated scoreboard run it again for even more relations (third time is not the charm, twice is enough!)

relationshipGoal = len(names) * (len(names) - 1)
while getNumRelations() < relationshipGoal : # the scoreboard is not complete, need to run more races 
	
	for horse in scoreboard :	
		if( len(scoreboard[horse]) < len(names) - 1 ) : # find the first horse which has an incomplete scoreboard
			relations = scoreboard[horse].keys()
			relations.append(horse)
			final = findUnrelatedHorses( relations )
			final.append(horse)
			result = race(final)
			#print('New ranking: ' + str(result))
			resultToScoreboard(race(final))
			break
	updateScoreboard()
	#print(getNumRelations())

print('It took ' + str(numRaces) + ' five-horse-races to rank all ' + str(len(names)) + ' horses')
