#include "gtest/gtest.h"
#include "matrix.h"

TEST(transposeTest, smallSquare)
{
#include "smallSquare.h"
#include "smallSquareTrans.h"
    
    int rows, cols;
    size_t dimension = sizeof(smallSquare)/sizeof(smallSquare[0]);
    rows = cols = dimension;
    
    Matrix* A = new Matrix(&smallSquare[0][0],
                           rows, cols);
    Matrix* B = new Matrix(&smallSquareTrans[0][0],
                           rows, cols);

    A->transpose();

	EXPECT_EQ(*A, *B);

    free(A);
}

