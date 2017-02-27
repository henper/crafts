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
#include <pthread.h>

void multiThreadedTranspose(void* instance);

/* Public stuff */

Matrix::Matrix(int* entry,
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
            std::printf("%3d ", this->entry[idx(row, col)]);
        }
        std::printf("\n");
    }
    std::printf("\n");
}

void Matrix::transpose(bool threaded) 
{
    swap(rows, cols); // This is pretty much all there is to transposing...
    
    numSwaps = 0; // Reset the bean-counter

    if( threaded )
        multiThreadedTranspose();
    else
        singleThreadedTranspose();

}

/* Private parts */

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

void Matrix::singleThreadedTranspose()
{
    // When we get to it, the last row will already be correct
    for(int row = 0; row < rows -1; row++)
    {
        // First column always correct when we get to it
        for(int col = 1; col < cols; col++)
        {
            // At this point we're at an element that's not yet where it should be
            int pills = col * ((rows - 1) - row); // this is how far away the value I want is
            numSwaps += pills;
            // Designate the value as the current 'PacMan' and it will eat its way over here
            poopingPacman(&entry[idx(row, col)], pills);
        }
    }
}

struct threadParams
{
    int* target;
    int  pills;
};

void Matrix::multiThreadedTranspose()
{
    static const int numThreads = 2;
    struct threadParams params[numThreads];
    pthread_t refs[numThreads];
    
    for(int row = 0; row < rows -1; row++)
    {
        for(int col = 1; col < cols + numThreads - 1; col += numThreads)
        {
            for(int thread = 0; thread < numThreads; thread++)
            {
                int myCol = col + thread;
                if(myCol < cols)
                {
                    params[thread].target = &entry[idx(row, myCol)];
                    params[thread].pills  = myCol * ((rows - 1) - row);
                    numSwaps += params[thread].pills;
                    
                    pthread_create(&refs[thread],
                                   NULL,
                                   threadEntryPoint,
                                   &params[thread]);
                }
            }
            for(int thread = 0; thread < numThreads; thread++)
            {
                pthread_join(refs[thread], NULL);
            }
        }
    }
}

void* Matrix::threadEntryPoint(void* params)
{
    struct threadParams* thread = (struct threadParams*)params;
    
    poopingPacman(thread->target, thread->pills);
    
    return NULL;
}
