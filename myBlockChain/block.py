'''
Created on Mar 5, 2019

@author: eponhik
'''
import unittest

# note to self, by see about aquiring Gordon Freemans suite
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.exceptions import InvalidSignature
from time import ctime

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
        except InvalidSignature :
            return False
        return True

class Block :    
    def __init__(self, prevHash, data=b"") :
        self.prevHash = prevHash
        self.timeStamp = ctime().encode('utf-8')
        self.data = data
        
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(self.data)
        digest.update(self.timeStamp)
        digest.update(self.prevHash)
        self.thisHash = digest.finalize()

class BlockChain :
    def __init__(self):
        self.blocks = [Block(b'0')]
        self.length = 1
    def __len__(self):
        return self.length
    def __getitem__(self,key):
        return self.blocks[key]
    def add(self, data=b""):
        lastIndex = len(self.blocks) - 1
        prevHash  = self.blocks[lastIndex].thisHash
        self.blocks.append(Block(prevHash, data))
        self.length = len(self.blocks)
    def validate(self):
        prevHash = b'0'
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
        genises = Block(b'0', b"Genisis")
        assert(genises.prevHash == b'0')

    def testNextBlock(self):
        genises  = Block(b'0', b"Genisis")
        nextGen  = Block(genises.thisHash, b"I am next")
        nextNext = Block(nextGen.thisHash, b"I am nextNext")
        
        print(nextGen.thisHash)
        print(nextNext.thisHash)
        
        assert(nextGen.prevHash == genises.thisHash)
        assert(nextNext.prevHash == nextGen.thisHash)
        
    def testValidate(self):
        blockChain = buildBlocks(3)
        assert(len(blockChain) == 3)
        assert(blockChain.validate())
        
        # tamper with the chain
        blockChain.blocks[1] = Block(blockChain[0].thisHash, b"All coins to Henrik")
        assert(blockChain.validate() == False)
        
    def testWallet(self):
        alice = Wallet()
        eve   = Wallet()

        data = b'all Alices money to Bob'
        wire = Transaction(data, alice.public_key, alice.sign(data))
        assert(wire.verify())

        hack = b'all Alices money to Eve'
        wire.data = hack
        assert(wire.verify() == False)
        wire = Transaction(hack, alice.public_key, eve.sign(hack))
        assert(wire.verify() == False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()