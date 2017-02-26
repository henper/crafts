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
    free(B);
}

TEST(transposeTest, smallRectangle)
{
#include "smallRectangle.h"
#include "smallRectangleTrans.h"
    
    int rows = sizeof(smallRectangle)/sizeof(smallRectangle[0]);
    int cols = sizeof(smallRectangle[0])/sizeof(smallRectangle[0][0]);
    
    Matrix* A = new Matrix(&smallRectangle[0][0],
                           rows, cols);
                           
    rows = sizeof(smallRectangleTrans)/sizeof(smallRectangleTrans[0]);
    cols = sizeof(smallRectangleTrans[0])/sizeof(smallRectangleTrans[0][0]);
    
    Matrix* B = new Matrix(&smallRectangleTrans[0][0],
                           rows, cols);

    A->transpose();

	EXPECT_EQ(*A, *B);

    free(A);
    free(B);
}

