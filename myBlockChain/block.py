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
    
    def __init__(self, prevHash, data="") :
        self.prevHash = prevHash
        self.timeStamp = time.ctime()
        self.data = data
        # concatenate data, prev hash, (nonce) and timestamp
        self.thisHash = hashlib.sha256(self.data + self.timeStamp + prevHash).hexdigest()

def buildBlocks(numBlocks) :
    blockChain = [Block('0')]
    for idx in range(1,numBlocks) :
        prevHash = blockChain[idx-1].thisHash
        blockChain.append(Block(prevHash))
    return blockChain

def validateBlocks(blockChain):
    prevHash = '0'
    for block in blockChain:
        if block.prevHash != prevHash :
            return False
        prevHash = block.thisHash
    return True

class Test(unittest.TestCase):


    def testGenisis(self):
        genises = Block('0', "Genisis")
        assert(genises.prevHash == '0')
        pass

    def testNextBlock(self):
        genises  = Block('0', "Genisis")
        nextGen  = Block(genises.thisHash, "I am next")
        nextNext = Block(nextGen.thisHash, "I am nextNext")
        
        print(nextGen.thisHash)
        print(nextNext.thisHash)
        
        assert(nextGen.prevHash == genises.thisHash)
        assert(nextNext.prevHash == nextGen.thisHash)
        
    def testValidate(self):
        blockChain = buildBlocks(3)
        assert(len(blockChain) == 3)
        assert(validateBlocks(blockChain))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()