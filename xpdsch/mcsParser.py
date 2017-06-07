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


mismatches = collections.deque()

for line in lines :
  mo = re.search('Mismatch for symbols_16\[(?P<sf>[0-9]*)\]\[(?P<symbol>[0-9]*)\]\[(?P<antenna>[0-9]*)\]\[(?P<re>[0-9]*)\] \((IM|RE)\), REF: (?P<ref>[-0-9]*), DUT: (?P<dut>[-0-9]*)', line)
  if mo :
    # Named tpules as key-value pair in dicttionary
    Mismatch = collections.namedtuple('Mismatch', ['subframe', 'symbol', 'antenna', 'element'])

    Mismatch.subframe = mo.group('sf')
    Mismatch.symbol   = mo.group('symbol')
    Mismatch.antenna  = mo.group('antenna')
    Mismatch.element  = mo.group('re')

    mismatches.append(Mismatch)

subframes = set([mismatch.subframe for mismatch in mismatches])
symbols   = set([mismatch.symbol   for mismatch in mismatches])
antennas  = set([mismatch.antenna  for mismatch in mismatches])
elements  = set([mismatch.element  for mismatch in mismatches])

print('Mismatches exist in the following: ')
print('subframes : ' + ', '.join(str(subframe) for subframe in subframes))
print('symbols   : ' + ', '.join(str(symbol)   for symbol   in symbols))
print('antennas  : ' + ', '.join(str(antenna)  for antenna  in antennas))
print('elements  : ' + ', '.join(str(element)  for element  in elements))
