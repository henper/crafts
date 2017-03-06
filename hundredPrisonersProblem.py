#!/usr/bin/python

'''
100 Prisoners will all be executed
unless they pick their number from
100 boxes. One by one, in a sealed
room. You only get to open half of
the boxes. If you havent found the
number you need, you are dead mate
'''

from random import shuffle

numPrisoners = 100
iterations   = 1000


def badStrategy(prisoner) :
    boxesToOpen = boxes
    shuffle(boxesToOpen)
    for boxToOpen in boxesToOpen[:numPrisoners/2] :
        if prisoner == boxes[boxToOpen] :
            return True
    return False
    
def goodStrategy(prisoner) :
    # See if the my number, N, is in the N:th box
    numberFound = boxes[ prisoner]
    boxesOpened = 1;
    while boxesOpened < numPrisoners/2 :
        if numberFound == prisoner :
            #I lived!
            return True
        numberFound = boxes[numberFound]
        boxesOpened += 1;
    return False
    
def prisonersOpen(boxes) :
    # Prisoners take turn opening boxes
    for prisoner in prisoners :
        if not goodStrategy(prisoner) :
            return 0
    return 1

# Assign all prisoners a number
prisoners = range(numPrisoners)

successes =  0.0
for iter in range(iterations) :
    # Put a random number in each box
    boxes = prisoners
    shuffle(boxes)
    successes += prisonersOpen(boxes)
print('Chance to survive: ' + str(successes/iterations))