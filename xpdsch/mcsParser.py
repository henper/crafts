#!/usr/bin/python

import sys
import re

if len(sys.argv) != 2 :
  print('Usage: ' + sys.argv[0] + ' <test.log>')
  exit()

lines = open(sys.argv[1])

mismatches = list()

for line in lines :
  mo = re.search('Mismatch for symbols_16\[(?P<sf>[0-9]*)\]\[(?P<symbol>[0-9]*)\]\[(?P<antenna>[0-9]*)\]\[(?P<re>[0-9]*)\] \((IM|RE)\), REF: (?P<ref>[-0-9]*), DUT: (?P<dut>[-0-9]*)', line)
  if mo :
    mismatches.append((mo.group('sf'),
                       mo.group('symbol'),
                       mo.group('antenna'),
                       mo.group('re'),
                       mo.group('ref'),
                       mo.group('dut')))

for mismatch in mismatches :
  print(mismatch)
