
#include "weak.h"
#include <primesieve.hpp>
#include <cstdio>

static inline void resetNumber(weakGoldbachNumbers &weakGoldbach, int number, int &idx)
{
  if(weakGoldbach.sum() > number)
    {
      weakGoldbach.numbers[idx] = 0;
      idx--;
    }
}

weakGoldbachNumbers calculateWeakGoldbachFor(int number)
{
  std::vector<int> primes;
  primesieve::generate_primes(number, &primes);

  primesieve::iterator it;
  it.skipto(number);

  // bad guess
  int currPrime = (int)it.prev_prime();
  weakGoldbachNumbers weakGoldbach = { 0 };

  const int maxIter = 10;
  int iter = 0;

  while(weakGoldbach.sum() != number)
  {
    // simple selector for number to work on
    int idx;
    for(idx = 0; idx < 3; idx++)
    {
      if(weakGoldbach.numbers[idx] == 0)
        break;
    }

    // reset numbers
    resetNumber(weakGoldbach, number, idx);
    resetNumber(weakGoldbach, number, idx);
    resetNumber(weakGoldbach, number, idx);

    if(weakGoldbach.sum() + currPrime <= number)
      weakGoldbach.numbers[idx] = currPrime;
    else
      weakGoldbach.numbers[idx] = currPrime = it.prev_prime(); 

    printf("iter: %4d numbers: %2d %2d %2d sum: %3d\n",
      iter++, weakGoldbach.numbers[0], weakGoldbach.numbers[1], weakGoldbach.numbers[2], weakGoldbach.sum());
    
    if(iter > maxIter)
      break;
  }
  
  return weakGoldbach;
}

  