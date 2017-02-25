#!/usr/bin/env python

'''
Disprove the Christian Goldbach hypothesis:
all odd composite numbers can be written as the sum of a 
prime and twice a square.

    oddComposite = prime + 2 * X^2

Also known as the OTHER Goldbach conjecture.
THE Goldbach conjecture was disproven in the previous version of this file

'''

from sympy import prime # SymbolicPython includes a nice way of getting prime-numbers

# initiate the prime directive
allPrimes = list() # that is smaller than the current oddComposite
primeIdx = 1
allPrimes.append(primeIdx)

def goldbach(oddComposite) :
    for prime in allPrimes :
        # try to find a twice square equal to oddComposite + prime
        X = 1
        while (prime +  2 * X**2) <= oddComposite :
            if oddComposite == (prime +  2 * X**2) :
                #print(str(oddComposite) + ' = ' + str(prime) + ' + ' + str(X) + '^2')
                return True
            X += 1
    return False

for primeIdx in range(1, 1000):

    # Add the next prime number to the list
    allPrimes.append(prime(primeIdx))

    # Test numbers from the prev prime up to the next prime
    lastPrimeIdx = len(allPrimes) - 1
    prevPrimeIdx = lastPrimeIdx - 1
    
    startingOddNumber = allPrimes[prevPrimeIdx] + 2 #primes themselves are odd.. and uneaven

    # exclude the prime itself
    lastNumber = allPrimes[lastPrimeIdx] - 1
    #print('The current test ranges from ' + str(startingOddNumber) + ' to ' + str(lastNumber))
    
    # Build the test range of odd numbers
    testRange = range(startingOddNumber, lastNumber, 2)
    
    # just do it!
    for oddComposite in testRange :
        if not goldbach(oddComposite) :
            print(str(oddComposite) + ' is not a Goldbach number!')
            exit()
