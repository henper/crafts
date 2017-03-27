#!/usr/bin/python

import random

# Generate 25 horses (no 2 horses are alike) with times between 50 and 100
horseList = [random.choice([i for i in xrange(50, 100)]) for r in xrange(25)]


def tournament(horsies) :

  # Group horses into heats of 5. Using list comprehension to create a list of lists
  heats = [horsies[i:i+5] for i in range(0, len(horsies), 5)]
  
  # To the Races!
  for heat in heats :
    heat.sort()

  # Show the leaderboards
  print(heats)
  print(len(heats))

tournament(horseList)
