#!/usr/bin/python

'''
The script that lies herein is henceforth to deduce meaning from the
mysterious and make clear what is not so.

I.e. if you've fucked up in DL MCS and get a a whole bunch of printouts like:
  
  Mismatch for symbols_16[49][13][1][1199] (RE), REF: 4663, DUT: 4661

this script can catalog in which symbols you done goofed and by how much.

'''

import sys
import re
import collections

# Give the log file to parse as argument
# if len(sys.argv) != 2 :
#   print('Usage: ' + sys.argv[0] + ' <test.log>')
#   exit()

# lines = open(sys.argv[1])
lines = open('test.log')

# Named tpules as key-value pair in dicttionary
Mismatch = collections.namedtuple('Mismatch', ['subframe', 'symbol', 'antenna', 'resourceElement'])

mismatches = collections.deque([Mismatch])

for line in lines :
  mo = re.search('Mismatch for symbols_16\[(?P<sf>[0-9]*)\]\[(?P<symbol>[0-9]*)\]\[(?P<antenna>[0-9]*)\]\[(?P<re>[0-9]*)\] \((IM|RE)\), REF: (?P<ref>[-0-9]*), DUT: (?P<dut>[-0-9]*)', line)
  if mo :
    Mismatch.subframe        = mo.group('sf')
    Mismatch.symbol          = mo.group('symbol')
    Mismatch.antenna         = mo.group('antenna')
    Mismatch.resourceElement = mo.group('re')

    mismatches.append(Mismatch)

for mismatch in mismatches :
  print(mismatch.symbol)
