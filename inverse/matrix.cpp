#include "matrix.h"
#include <cstring>

Matrix::Matrix(int* entries,
               int rows,
               int cols)
{
    this->entries = entries;
    this->rows = rows;
    this->cols = cols;
}

bool operator==(const Matrix& lhs, const Matrix& rhs)
{
    return false;
}

void Matrix::inverse()
{
    
}