#include "gtest/gtest.h"
#include "matrix.h"

TEST(inverseTest, smallMatrix)
{
	int origin[][3] =
	{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	};
    Matrix* A = new Matrix(&origin[0][0], 3, 3);
    A->print();
    
    int expect[][3] =
	{
		{1, 4, 7},
		{2, 5, 8},
		{3, 6, 9},
	};
    Matrix B = Matrix(&expect[0][0], 3, 3);
    B.print();
    
    A->inverse();
    A->print();

	EXPECT_EQ(*A, B);
    
    free(A);
}

TEST(inverseTest, slightlyLargerMatrix)
{
	int origin[][4] =
	{
		{ 1,  2,  3,  4},
		{ 5,  6,  7,  8},
		{ 9, 10, 11, 12},
        {13, 14, 15, 16}
	};
    Matrix A = Matrix(&origin[0][0], 4, 4);
    A.print();
    
    int expect[][4] =
	{
		{ 1, 5,  9, 13},
		{ 2, 6, 10, 14},
		{ 3, 7, 11, 15},
        { 4, 8, 12, 16}
	};
    Matrix B = Matrix(&expect[0][0], 4, 4);
    B.print();
    
    A.inverse();
    A.print();

	EXPECT_EQ(A, B);
}
