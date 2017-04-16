#!/usr/bin/python

#import random
from collections import defaultdict
import matplotlib.pyplot as plt
import codecs

numRaces = 0

# Generate times for horses (no 2 horses are alike) with 2-digit times (for easy printing)
#times = [random.choice([i for i in xrange(10, 99)]) for r in xrange(len(names))]
times = [107,47,102,64,50,100,28,91,27,5,22,114,23,42,13,3,93,8,92,79,53,83,63,7,15,66,105,57,14,65,58,113,112,1,62,103,120,72,111,51,9,36,119,99,30,20,25,84,16,116,98,18,37,108,10,80,101,35,75,39,109,17,38,117,60,46,85,31,41,12,29,26,74,77,21,4,70,61,88,44,49,94,122,2,97,73,69,71,86,45,96,104,89,68,40,6,87,115,54,123,125,90,32,118,52,11,33,106,95,76,19,82,56,121,55,34,24,43,124,81,48,110,78,67,59]

# Create a list of names to use as dictionary keys
fh = codecs.open('moreHorses.txt', encoding='utf-8')
lines = fh.readlines()
lines = lines[0:len(times)]
names = [line.rstrip() for line in lines]
horses = set(names)

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
  return sum([len(scoreboard[horse]) for horse in scoreboard])

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
  rankings = range(len(horses))
  for horse in horses :
    rankings[sum(scoreboard[horse].values())] = horseTimes[horse]
  return rankings

def printRaceResults( result ) :
  for horse in result :
    print(horse + ': ' + str(horseTimes[horse]))

def mostConnectedIn( horseList ) : #but not completely connected
    # Sort the horses according to their connections
  connections = [(len(scoreboard[horse]), horse) for horse in horseList]
  connections.sort()
  connections.reverse()

  # Find the most connected, but not complete horse
  for horseTuple in connections :
    if horseTuple[0] < len(horses) - 1 :
      return horseTuple[1]
      break
  #print(str(horseList) + 'only have completed connections')
  return None

def mostConnectedAndUnrelatedIn( horseSet ) :
  goldenBoy = mostConnectedIn(horseSet)
  goldenBoyRelations = set(scoreboard[goldenBoy].keys())
  goldenBoyRelations.add(goldenBoy) # any horse is by definition its own relative
  unrelated = horseSet - goldenBoyRelations
  return (goldenBoy, unrelated)

relationshipGoal = len(names) * (len(names) - 1)

# plot stuff
#plt.xkcd() #heh
fig, ax = plt.subplots(figsize=(20, 10), ncols=2)
fig.set_figheight(10)
fig.set_figwidth(20)

# Set up the canvas, the ranges here decides the elements to plot and y axis ranges (if not limited)
xticks = 226 #max number of races
yrange = [0 for i in range(xticks)]; yrange[len(yrange)-1] = relationshipGoal
line = ax[0].plot(range(xticks), yrange, animated=True)
bars = ax[1].bar(times, range(125), animated=True)

# Let's capture the background of the figure
backgrounds = [fig.canvas.copy_from_bbox(axe.bbox) for axe in ax]

ax[0].set_title ('Total relations (goal=15500)')
ax[0].set_xlabel('# five-horse races')
ax[0].set_ylabel('# horse relations')
ax[0].set_xlim([0, xticks])
ax[0].set_ylim([0, relationshipGoal])

ax[1].set_title( 'Individual relations (goal=124)')
ax[1].set_xlabel('Horse time')
ax[1].set_ylabel('# horse relations')
ax[1].set_xlim([1, len(horses)])
ax[1].set_ylim([min(times), max(times)])

fig.show()
fig.canvas.draw()

numRelations = 0; relationsList = [0 for i in range(xticks)]
while numRelations < relationshipGoal : # the scoreboard is not complete, need to run more races 
  try :
    # Plot stuff
    paint = 'blue'
    dot = 'o'

    # Actual algo.
    intersection = horses
    lineup = ['', '', '', '', '']
    for position in range(len(lineup)) :
      lineup[position], intersection = mostConnectedAndUnrelatedIn(intersection)
      if lineup[position] == None :
        paint = 'red'; dot = '*' # signify failiure to get a perfect race
        del(lineup[position:])
        break

    result = race(lineup)
    #printRaceResults(result)
    resultToScoreboard(result)
    updateScoreboard()
    #numRelations = getNumRelations() # calculated by plot stuff

    # more plot stuff

    # bar graph with a bar for each horse('s time') and how many relatives it has
    heights = [len(scoreboard[horse]) for horse in names]
    numRelations = sum(heights)

    fig.canvas.restore_region(backgrounds[1])
    for  idx in range(125) :
      bars[idx].set_height(heights[idx])
      ax[1].draw_artist(bars[idx])
    fig.canvas.blit(ax[1].bbox)

    # scatter plot
    fig.canvas.restore_region(backgrounds[0])
    relationsList[numRaces] = numRelations
    line[0].set_ydata(relationsList)
    ax[0].draw_artist(line[0])
    fig.canvas.blit(ax[0].bbox)
    #ax[0].scatter(numRaces, numRelations, color=paint, marker=dot)

    #fig.canvas.blit(ax[0].bbox)
    #fig.canvas.draw()

  except KeyboardInterrupt:
    break


print('It took ' + str(numRaces) + ' five-horse-races to rank all ' + str(len(names)) + ' horses')
print(str(ranking()))
