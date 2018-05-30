#include <cstdio>
#include <gtest/gtest.h>
#include "weak.h"

TEST(WeakTest, eleven)
{
  weakGoldbachNumbers weakGoldbach = calculateWeakGoldbachFor(11);
  EXPECT_EQ(weakGoldbach.numbers[0], 5);
  EXPECT_EQ(weakGoldbach.numbers[1], 3);
  EXPECT_EQ(weakGoldbach.numbers[2], 3);
}

TEST(WeakTest, thirtyfive)
{
  weakGoldbachNumbers weakGoldbach = calculateWeakGoldbachFor(35);
  EXPECT_EQ(weakGoldbach.numbers[0], 19);
  EXPECT_EQ(weakGoldbach.numbers[1], 13);
  EXPECT_EQ(weakGoldbach.numbers[2],  3);
}
