'''
Created on Mar 5, 2019

@author: eponhik
'''
import unittest

# note to self, by see about aquiring Gordon Freemans suite
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_public_key
from cryptography.exceptions import InvalidSignature
from time import ctime
import json

class Wallet:
    def __init__(self):
        self.private_key = dsa.generate_private_key( key_size=1024, backend=default_backend() )
        self.public_key  = self.private_key.public_key()
    def id(self):
        return self.public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo).decode('utf-8')
    def sign(self, transaction):
        return self.private_key.sign(transaction.serialize(), hashes.SHA256())

class Transaction:
    def __init__(self, sender, amount, receiver, signature=b''):
        self.sender = sender
        self.amount = amount
        self.receiver = receiver
        self.signature = signature
    def __eq__(self, other):
        return (self.sender == other.sender and
                self.amount == other.amount and
                self.receiver == other.receiver and
                self.signature == other.signature)
    def verify(self):
        publicKey = load_pem_public_key(self.sender.encode('utf-8'), backend=default_backend())
        try:
            publicKey.verify(self.signature, self.serialize(), hashes.SHA256())
        except InvalidSignature :
            return False
        return True
    def serialize(self):
        meta = {'sender': self.sender, 'amount': self.amount, 'receiver': self.receiver}
        return json.dumps(meta, indent=4, sort_keys=True).encode('utf-8')
    @classmethod
    def deserialize(object, serialized):
        return(Transaction(**json.loads(serialized.decode('utf-8'))))
    def pack(self):
        packed = bytes() # the signature is a pure byte object and not decodable, append it to the serialized object
        return packed.join([self.serialize(), self.signature])
    @classmethod
    def unpack(obj, packed):
        # the metadata is in a dictionary which ends with a curlybracket, split there to get both metadata and signature
        [meta, sep, signature] = packed.partition(b'}')
        obj = Transaction.deserialize(meta+sep)
        obj.signature = signature
        return obj

class Block :    
    def __init__(self, prevHash, transaction=b"") :
        self.prevHash = prevHash
        self.timeStamp = ctime().encode('utf-8')
        self.transaction = transaction
        
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(self.transaction)
        digest.update(self.timeStamp)
        digest.update(self.prevHash)
        self.thisHash = digest.finalize()

class BlockChain :
    def __init__(self, block=Block(b'0')):
        self.blocks = [block]
        self.length = 1
    def __len__(self):
        return self.length
    def __getitem__(self,key):
        return self.blocks[key]
    def add(self, transaction=b""):
        lastIndex = len(self.blocks) - 1
        prevHash  = self.blocks[lastIndex].thisHash
        self.blocks.append(Block(prevHash, transaction))
        self.length = len(self.blocks)
        return True
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

        assert(nextGen.prevHash == genises.thisHash)
        assert(nextNext.prevHash == nextGen.thisHash)

    def testValidate(self):
        blockChain = buildBlocks(3)
        assert(len(blockChain) == 3)
        assert(blockChain.validate())
        
        # tamper with the chain
        blockChain.blocks[1] = Block(blockChain[0].thisHash, b"All coins to Henrik")
        assert(blockChain.validate() == False)

    def testTransactionVerification(self):
        alice = Wallet()
        bob   = Wallet()
        eve   = Wallet()

        wire = Transaction(alice.id(), 10.5, bob.id())
        wire.signature = alice.sign(wire)
        assert(wire.verify())

        # intercept
        wire.receiver = eve.id()
        assert(wire.verify() == False)

        # inject
        hack = Transaction(alice.id(), 10.5, eve.id())
        hack.signature = alice.sign(wire)
        assert(wire.verify() == False)

    def testTransactionSerdes(self):
        alice = Wallet()
        bob   = Wallet()

        wire = Transaction(alice.id(), 10.5, bob.id())

        serialized = wire.serialize()
        deserialized = Transaction.deserialize(serialized)
        assert(wire == deserialized)

        wire.signature = alice.sign(wire)

        packed = wire.pack()
        unpacked = Transaction.unpack(packed)
        
        assert(wire == unpacked)

    def testBlockChainOfTransactions(self):
        cornucopia = Wallet()
        alice = Wallet()

        allTheMonies = 1024*1024 #should be enough for everyone
        wire = Transaction(cornucopia.id(), allTheMonies, alice.id())
        wire.signature = cornucopia.sign(wire)

        # to create a ledgible ledger it'd help with names from id's
        names = {cornucopia.id(): 'cornucopia', alice.id(): 'alice'} 
        cornucopia = None # no inflation zone

        blockChain = BlockChain(Block(b'0', wire.pack()))

        # add frindly user and transfer some monies
        bob = Wallet()
        names.update({bob.id(): 'bob'})

        wire = Transaction(alice.id(), 10.5, bob.id())
        assert(blockChain.add(wire.pack()))

        # pretty print the current balance of all users
        ledger = dict()
        for block in blockChain :
            transaction = Transaction.unpack(block.transaction)

            # update receiver
            if(ledger.get(transaction.receiver)):
                # user already in ledger
                ledger.update({transaction.receiver: ledger.get(transaction.receiver)+transaction.amount})
            else:
                # welcome to the game
                ledger.update({transaction.receiver: transaction.amount})

            #update sender
            if(ledger.get(transaction.sender)):
                # user already in ledger
                ledger.update({transaction.sender: ledger.get(transaction.sender)-transaction.amount})
            else:
                # welcome to the game (genisis block only!)
                ledger.update({transaction.sender: -transaction.amount})

        ledgibleLedger = dict()
        for key in names.keys():
            ledgibleLedger.update({names[key]: ledger[key]})
        print(json.dumps(ledgibleLedger, indent=4, sort_keys=True))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()