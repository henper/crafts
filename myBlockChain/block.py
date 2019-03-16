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
from math import log, ceil
import json

DIFFICULTY = '000'

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

class Block :    
    def __init__(self, prevHash, transactions=[Transaction('foo', 1, 'bar')]) :
        self.prevHash = prevHash
        self.timeStamp = ctime().encode('utf-8')
        self.transactions = transactions
        
        # pre-hash the knowns so we only do that the one time
        preDigested = self.__preDigest()
        
        # Do proof-of work by finding a hash that ends with difficulty
        self.difficulty = DIFFICULTY
        self.thisHash = b'1' # init hash with anything that doesn't satisfy difficulty
        self.nonce = 0
        
        # find a nonce-value that will satisfy the difficulty
        while(self.thisHash.hex().endswith(self.difficulty) == False):
            digest = preDigested.copy()
            self.nonce = self.nonce +1
            bytesToStoreNonce = ceil(log(self.nonce+1)/log(2)/8)
            digest.update(self.nonce.to_bytes(bytesToStoreNonce, byteorder='big'))
            self.thisHash = digest.finalize()
            #print(self.thisHash.hex())

    def __preDigest(self):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        
        for transaction in self.transactions :
            digest.update(transaction.serialize())
            digest.update(transaction.signature)
        
        digest.update(self.timeStamp)
        digest.update(self.prevHash)
        return digest

class BlockChain :
    genisisHash = b'0'
    def __init__(self, block=Block(genisisHash)):
        self.blocks = [block]
        self.length = 1
    def __len__(self):
        return self.length
    def __getitem__(self,key):
        return self.blocks[key]
    def add(self, transactions):
        
        if self.__verifyTransactions(transactions) == False:
            return False

        lastIndex = len(self.blocks) - 1
        prevHash  = self.blocks[lastIndex].thisHash
        self.blocks.append(Block(prevHash, transactions))
        self.length = len(self.blocks)
        return True
    def __verifyTransactions(self, transactions):
        for transaction in transactions :
        # verify the transaction signature
            if(transaction.verify() == False):
                print('ERROR: Transaction signature validation failed!')
                return False
    
            # verify sender has the necessary monies
            ledger = self.ledger()
            if(transaction.sender in ledger):
                funds = ledger[transaction.sender]
                if(funds < transaction.amount):
                    print('ERROR: Sender has only ' + str(funds) + ' monies!')
                    return False
            else:
                print('ERROR: Sender has never received any monies!')
                return False
        
        # all checks Ok
        return True
    def validate(self):
        prevHash = genisisHash
        for block in self.blocks:
            if block.prevHash != prevHash :
                return False
            prevHash = block.thisHash
        return True
    def ledger(self): # build a dictionary of all users bottom line
        ledger = dict()
        for block in self.blocks :
            for transaction in block.transactions :
                # update receiver
                if(transaction.receiver in ledger):
                    # user already in ledger
                    ledger.update({transaction.receiver: ledger[transaction.receiver]+transaction.amount})
                else:
                    # welcome to the game
                    ledger.update({transaction.receiver: transaction.amount})
                #update sender
                if(transaction.sender in ledger):
                    # user already in ledger
                    ledger.update({transaction.sender: ledger[transaction.sender]-transaction.amount})
                else:
                    # welcome to the game (genisis block only!)
                    ledger.update({transaction.sender: -transaction.amount})
        return ledger

# vestige convenience function
def buildBlocks(numBlocks) :
    blockChain = BlockChain()
    for idx in range(1,numBlocks) :
        blockChain.add()
    return blockChain   

class Test(unittest.TestCase):


    def testGenisis(self):
        genises = Block(b'0')
        assert(genises.prevHash == b'0')
        assert(genises.thisHash.hex().endswith(DIFFICULTY))

    def testNextBlock(self):
        genises  = Block(b'0')
        nextGen  = Block(genises.thisHash)
        nextNext = Block(nextGen.thisHash)

        assert(nextGen.prevHash == genises.thisHash)
        assert(nextNext.prevHash == nextGen.thisHash)

    #def testValidate(self):
        #blockChain = buildBlocks(3)
        #assert(len(blockChain) == 3)
        #assert(blockChain.validate())
        
        # tamper with the chain
        #blockChain.blocks[1] = Block(blockChain[0].thisHash, b"All coins to Henrik")
        #assert(blockChain.validate() == False)

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

    def testBlockChainOfTransactions(self):
        cornucopia = Wallet()
        alice = Wallet()

        allTheMonies = 1024*1024 #should be enough for everyone
        wire = Transaction(cornucopia.id(), allTheMonies, alice.id())
        wire.signature = cornucopia.sign(wire)

        # to create a ledgible ledger it'd help with names from id's
        names = {cornucopia.id(): 'cornucopia', alice.id(): 'alice'} 
        cornucopia = None # no inflation zone

        blockChain = BlockChain(Block(b'0', [wire]))

        # add frindly user and transfer some monies
        bob = Wallet()
        names.update({bob.id(): 'bob'})

        wire = Transaction(alice.id(), 10.5, bob.id())
        assert(blockChain.add([wire]) == False) # unsigned!
        wire.signature = alice.sign(wire)
        assert(blockChain.add([wire]))
        

        # add an unfriendly user and try to transfer more monies than exists
        eve = Wallet()
        names.update({eve.id(): 'eve'})

        wire = Transaction(bob.id(), 11, eve.id())
        wire.signature = bob.sign(wire)
        assert(blockChain.add([wire]) == False)

        print('Blocks in chain: ' + str(len(blockChain)))
        # pretty print the current balance of all users
        ledger = blockChain.ledger()
        ledgibleLedger = dict()
        for key in names.keys():
            if(key in ledger):
                ledgibleLedger.update({names[key]: ledger[key]})
        print(json.dumps(ledgibleLedger, indent=4, sort_keys=True))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()