#include "gtest/gtest.h"
#include "matrix.h"

TEST(transposeTest, tinySquareMatrix)
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
    Matrix* B = new Matrix(&expect[0][0], 3, 3);
    
    A->transpose();
    A->print();
    printf("A %d by %d matrix took %d swaps to transpose.\n",
           A->rows, A->cols, A->numSwaps);

  EXPECT_EQ(*A, *B);
    
    free(A);
    free(B);
}

TEST(transposeTest, tinyRectangularMatrix)
{
  int origin[][4] =
  {
    { 1,  2,  3,  4},
    { 5,  6,  7,  8},
    { 9, 10, 11, 12}
  };
    Matrix* A = new Matrix(&origin[0][0], 3, 4);
    A->print();
    
    int expect[][3] =
  {
    { 1, 5,  9},
    { 2, 6, 10},
    { 3, 7, 11},
    { 4, 8, 12}
  };
    Matrix* B = new Matrix(&expect[0][0], 4, 3);
    
    A->transpose();
    A->print();
    printf("A %d by %d matrix took %d swaps to transpose.\n",
           A->cols, A->rows, A->numSwaps);

  EXPECT_EQ(*A, *B);

  free(A);
  free(B);
}

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
    printf("A %d by %d matrix took %d swaps to transpose.\n",
           cols, rows, A->numSwaps);

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
    printf("A %d by %d matrix took %d swaps to transpose.\n",
           cols, rows, A->numSwaps);

  EXPECT_EQ(*A, *B);

    free(A);
    free(B);
}

