'''
Created on Mar 29, 2019

@author: eponhik
'''
import unittest
from math import pow

slotTimeInSeconds = 125 * pow(10, -6)
symbolsInSlot = 14
resPerPrb = 12
  
slotsInTddPattern = 160
ssbSlots = 6

tdd4_1Pattern = {'numPdcchSymbols': (1+2/10) * slotsInTddPattern, # every slot has a pdcch symbol, 2 out of 10 has an additional symbol
                 'numPdschSymbols': (57 * 13 + 30 * 12 + 32 * 9 + 3 * 7), # 57 slots with 13 symbols, 30 with 12, 32 with 9 and 3 with 7
                 'numSsbSymbols'  : (4*12), # 4 symbols for every wideBeam
                 'numTrsSymbols'  : (6*3)}  # for some reason it takes 6 symbols to loop over 4 wide beams

ssbPrbsPerSymbol = 20
trsPrbsPerSymbol = 66 # TODO

pdcchPrbsPerSymbol = {66 : 48, # in 100 MHz cells 48 PRBs are used for PDCCH 
                      32: 24}  # in  50 MHz cells 48 PRBs are used for PDCCH

bwInMhz2Prbs = {100 : 66,
                 50 : 32}

class Highband():
    # Bandwidth in MHz, iqFormat in bits per resource element
    def __init__(self, bandwidth=100, layers=2, iqFormat=32, tddPattern = tdd4_1Pattern):
        self.bandwidth = bandwidth
        self.prbs = bwInMhz2Prbs.get(bandwidth)
        self.layers = layers
        self.iqFormat = iqFormat
        self.tddPattern = tddPattern

    def calcGrossBandwidth(self):
        return (self.prbs * resPerPrb * self.layers * self.iqFormat) / (slotTimeInSeconds / symbolsInSlot)

    # Maximum bandwidth not 
    def calcNetFronthaulBw(self):
        return (self.calcDlPrbsInPattern() * resPerPrb * self.layers * self.iqFormat) / (slotTimeInSeconds * slotsInTddPattern)

    def calcDlPrbsInPattern(self):
        prbsInPattern = 0
        prbsInPattern = prbsInPattern + self.tddPattern.get('numPdschSymbols') * self.prbs
        prbsInPattern = prbsInPattern + self.tddPattern.get('numPdcchSymbols') * pdcchPrbsPerSymbol.get(self.prbs)
        prbsInPattern = prbsInPattern + self.tddPattern.get('numSsbSymbols') * ssbPrbsPerSymbol
        prbsInPattern = prbsInPattern + self.tddPattern.get('numTrsSymbols') * trsPrbsPerSymbol
        return prbsInPattern
    
    def prettyPrint(self):
        print('Configuration: ' + str(self.bandwidth) + ' MHz, ' + str(self.layers) + ' layers, ', str(self.iqFormat) + ' bits/RE')
        print('Gross fronthaul bandwidth requirement: ' + str(self.calcGrossBandwidth() / pow(10,9)) + ' Gbps')
        print('Net downlink fronthaul bandwidth requirement: ' + str(self.calcNetFronthaulBw() / pow(10,9)) + ' Gbps')


class Test(unittest.TestCase):

    def testDefault(self):
        hb = Highband()
        hb.prettyPrint()
                
        assert(hb.calcDlPrbsInPattern() < bwInMhz2Prbs.get(hb.bandwidth) * symbolsInSlot * slotsInTddPattern)
        assert(hb.calcNetFronthaulBw() < hb.calcGrossBandwidth())
        
    def testBlockFloatingPointFormatAkinToC1FD(self):
        hb = Highband(iqFormat=9+9+2)
        hb.prettyPrint()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()