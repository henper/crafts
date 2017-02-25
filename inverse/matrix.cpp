#include "matrix.h"
#include <cstring>
#include <cstdio>

Matrix::Matrix(int* entry,
               int  rows,
               int  cols)
{
    this->entry = entry;
    this->rows = rows;
    this->cols = cols;
}

bool operator==(const Matrix& lhs, const Matrix& rhs)
{
    if(lhs.cols == rhs.cols &&
       lhs.rows == rhs.rows &&
       0 == std::memcmp(lhs.entry,
                        rhs.entry,
                        lhs.cols * rhs.rows * sizeof(int)))
        return true;

    return false;
}

void Matrix::print()
{
    for(int row = 0; row < this->rows; row++)
    {
        for(int col = 0; col < this->cols; col++)
        {
            std::printf("%3d ", this->entry[idx(row, col)]);
        }
        std::printf("\n");
    }
    std::printf("\n");
}

void Matrix::inverse()
{
    // the last row is correct already(?)
    for(int row = 0; row < this->rows -1; row++)
    {
        // first column always correct
        for(int col = 1; col < this->cols; col++)
        {
            int offset = col * ((this->rows - 1) - row);
            shift(&this->entry[idx(row, col)], offset);
        }
    }
}

/* Move a value in an array from an offset
 * to the top of the pile, whilst shifting
 * all the values in between down one step
 */
void Matrix::shift(int *target, int fromOffset)
{
    for(int i = fromOffset; i > 0; i--)
    {
        swap(target[i-1], target[i]);
    }
}

void Matrix::swap(int &a, int &b)
{
    int c = a;
    a = b;
    b = c;
}

int  Matrix::idx(int row, int col)
{
    return col + row*this->rows;
}
