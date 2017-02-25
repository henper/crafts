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
    Matrix A = Matrix(&origin[0][0], 3, 3);  
    
    int expect[][3] =
	{
		{1, 4, 7},
		{2, 5, 8},
		{3, 6, 9},
	};
    Matrix B = Matrix(&expect[0][0], 3, 3);

	EXPECT_EQ(A, B);
}
