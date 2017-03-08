/**
    SW-CoP, matrix.cpp

    Distributed on GitHub:
    https://github.com/henper/crafts

    Purpose: memory efficient
             matrix operation

    @author Henrik L. Persson
*/

#include "matrix.h"
#include <cstring>
#include <cstdio>

/* Public stuff */

Matrix::Matrix(quadRgb* entry,
               int  rows,
               int  cols)
{
    this->entry = entry;
    this->rows = rows;
    this->cols = cols;
    numSwaps = 0;
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
            std::printf("%3f ", this->entry[idx(row, col)].quadColor[0].r);
        }
        std::printf("\n");
    }
    std::printf("\n");
}

int Matrix::transpose() 
{    
    static int row = 0;
    static int col = 1;
    static int pills = col * ((rows - 1) - row); // this is how far away the value I want is

    //swap(rows, cols); // This is pretty much all there is to transposing...

    // When we get to it, the last row will already be correct
    if(row < rows -1)
    {
        // First column always correct when we get to it
        if(col < cols)
        {
            // At this point we're at an element that's not yet where it should be

            // Designate the value as the current 'PacMan' and it will eat its way over here
            //poopingPacman(&entry[idx(row, col)], pills);
            quadRgb *target = &entry[idx(row, col)];

            if(pills > 0)
            {
                swap(target[pills-1], target[pills]);
                pills--;
            }
            else
            {
                col++;
                pills = col * ((rows - 1) - row);   
            }
        }
        else
        {
            row++;
            col=0;
            pills = col * ((rows - 1) - row);
        }
    }

    return numSwaps;
}

int Matrix::sqrTranspose()
{
    static int width = 0;
    static int diag = width + 1;

    if( width < rows - 1)
    {
        if(diag < rows)
        {
            swap(entry[idx(width, diag)], entry[idx( diag, width)]);
            diag++;
        }
        else
        {
            width++;
            diag = width + 1;
        }
    }
    return numSwaps;
}

/* Private parts */

/* Move a value in an array from an offset
 * to the top of the pile, whilst shifting
 * all the values in between down one step
 */
void Matrix::poopingPacman(quadRgb *target, int pills)
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

void Matrix::swap(quadRgb &a, quadRgb &b)
{
    /*// Look Ma' -no hands!
    a = a xor b;
    b = a xor b;
    a = a xor b;*/

    quadRgb c;
    c = a;
    a = b;
    b = c;
    
    numSwaps++;
}

int  Matrix::idx(int row, int col)
{
    return col + row*this->cols;
}
