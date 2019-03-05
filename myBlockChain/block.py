'''
Created on Mar 5, 2019

@author: eponhik
'''
import unittest
import hashlib
import time

class Block :
    prevHash = 0
    thisHash = 0
    data = ""
    timeStamp = 0
    
    def __init__(self, data, prevHash=0) :
        self.prevHash = prevHash
        # concatenate data, prev hash, nonce and timestamp
        concat = data + time.ctime() + str(prevHash) #TODO nonce
        self.thisHash = hashlib.sha256(concat)

class Test(unittest.TestCase):


    def testGenisis(self):
        genises = Block("Genisis")
        assert(genises.prevHash == 0)
        pass

    def testNextBlock(self):
        genises  = Block("Genisis")
        nextGen  = Block("I am next", genises.thisHash)
        nextNext = Block("I am nextNext", nextGen.thisHash)
        
        assert(nextGen.prevHash == genises.thisHash)
        assert(nextNext.prevHash == nextGen.thisHash)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()