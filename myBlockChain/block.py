'''
Created on Mar 5, 2019

@author: eponhik
'''
import unittest
import hashlib # TODO replace with cryptography hash
import time

# note to self, by see about aquiring Gordon Freemans suite
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

class Wallet:
    def __init__(self):
        self.private_key = dsa.generate_private_key( key_size=1024, backend=default_backend() )
        self.public_key  = self.private_key.public_key()
    def sign(self, data):
        return self.private_key.sign(data, hashes.SHA256())

class Transaction:
    def __init__(self, data, publicKey, signature):
        self.publicKey = publicKey
        self.signature = signature
        self.data = data
    def verify(self):
        try:
            self.publicKey.verify(self.signature, self.data, hashes.SHA256())
        except cryptography.exceptions.InvalidSignature :
            return False
        return True

class Block :    
    def __init__(self, prevHash, data="") :
        self.prevHash = prevHash
        self.timeStamp = time.ctime()
        self.data = data
        # concatenate data, prev hash, (nonce) and timestamp
        concat = self.data + self.timeStamp + prevHash
        self.thisHash = hashlib.sha256(concat.encode('utf-8')).hexdigest()

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

# vestige convenience function
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
        
    def testWallet(self):
        alice = Wallet()
        eve   = Wallet()

        data = b'all Alices money to Bob'
        wire = Transaction(data, alice.public_key, alice.sign(data))

        assert(wire.verify())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()