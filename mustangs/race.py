#!/usr/bin/python

#import random
from collections import defaultdict
import codecs

numRaces = 0

# Generate times for horses (no 2 horses are alike) with 2-digit times (for easy printing)
#times = [random.choice([i for i in xrange(10, 99)]) for r in xrange(len(names))]
times = [107,47,102,64,50,100,28,91,27,5,22,114,23,42,13,3,93,8,92,79,53,83,63,7,15,66,105,57,14,65,58,113,112,1,62,103,120,72,111,51,9,36,119,99,30,20,25,84,16,116,98,18,37,108,10,80,101,35,75,39,109,17,38,117,60,46,85,31,41,12,29,26,74,77,21,4,70,61,88,44,49,94,122,2,97,73,69,71,86,45,96,104,89,68,40,6,87,115,54,123,125,90,32,118,52,11,33,106,95,76,19,82,56,121,55,34,24,43,124,81,48,110,78,67,59]

# Create a list of names to use as dictionary keys
fh = codecs.open('moreHorses.txt', encoding='utf-8')
lines = fh.readlines()
lines = lines[0:len(times)-1]
names = [line.rstrip() for line in lines]


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

def ranking() :
  ranking = range(len(scoreboard))
  timeTbl = range(len(ranking))
  for horse in scoreboard :
    ranking[ sum(scoreboard[horse].values()) ] = horse
  for rank in range(len(ranking)) :
    timeTbl[rank] = horseTimes[ranking[rank]];
  return timeTbl

def printRaceResults( result ) :
	for horse in result :
		print()

relationshipGoal = len(names) * (len(names) - 1)
while getNumRelations() < relationshipGoal : # the scoreboard is not complete, need to run more races 
  
  # Sort the horses according to their connections
  connections = [(len(scoreboard[horse]), horse) for horse in names]
  connections.sort()

  # Find the most connected, but not complete horse
  for horseTuple in reversed(connections) :
  	if horseTuple[0] < len(names) :
  		mostConnectedNotCompleteHorse = horseTuple[1]
  		break

  # Race the most connected horse against the 4 least connected

  result = race([connections[0][1],
                 connections[1][1],
                 connections[2][1],
                 connections[3][1],
                 mostConnectedNotCompleteHorse])
  resultToScoreboard(result)
  updateScoreboard()
  print(getNumRelations())


print('It took ' + str(numRaces) + ' five-horse-races to rank all ' + str(len(names)) + ' horses')
print(str(ranking()))
