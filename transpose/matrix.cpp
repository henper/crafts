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

void Matrix::transpose() 
{
    this->swap(rows, cols);
    // When we get to it, the last row will already be correct
    for(int row = 0; row < this->rows -1; row++)
    {
        // first column always correct when we get to it
        for(int col = 1; col < this->cols; col++)
        {
            int pills = col * ((this->rows - 1) - row);
            poopingPacman(&this->entry[idx(row, col)],
                          pills);
        }
    }
}

/* Move a value in an array from an offset
 * to the top of the pile, whilst shifting
 * all the values in between down one step
 */
void Matrix::poopingPacman(int *target, int pills)
{
    for(int i = pills; i > 0; i--)
    {
        swap(target[i-1], target[i]);
    }
}

void Matrix::swap(int &a, int &b)
{
    // Look Ma' -no hands!
    a = a xor b;
    b = a xor b;
    a = a xor b;
}

int  Matrix::idx(int row, int col)
{
    return col + row*this->cols;
}
