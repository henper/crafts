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

class BlockChain :
    def __init__(self):
        self.blocks = [Block('0')]
        self.length = 1
    def __len__(self):
        return self.length
    def __getitem__(self,key):
        return self.blocks[key]
    def add(self, data=""):
        lastIndex = len(self.blocks) - 1
        prevHash  = self.blocks[lastIndex].thisHash
        self.blocks.append(Block(prevHash, data))
        self.length = len(self.blocks)
    def validate(self):
        prevHash = '0'
        for block in self.blocks:
            if block.prevHash != prevHash :
                return False
            prevHash = block.thisHash
        return True

def buildBlocks(numBlocks) :
    blockChain = BlockChain()
    for idx in range(1,numBlocks) :
        blockChain.add()
    return blockChain   

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
        assert(blockChain.validate())
        
        # tamper with the chain
        blockChain.blocks[1] = Block(blockChain[0].thisHash, "All coins to Henrik")
        assert(blockChain.validate() == False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()