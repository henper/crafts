'''
Created on Mar 5, 2019

@author: eponhik
'''
import unittest
import hashlib

class Block :
    prevHash = 0
    thisHash = 0
    data = ""
    timeStamp = 0
    
    def __init__(self, prevHash, data) :
        self.prevHash = prevHash
        self.thisHash = hashlib.sha256(data)


class Test(unittest.TestCase):


    def testName(self):
        genisesBlock = Block(0, "Genisis")
        assert(genisesBlock.prevHash == 0)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()