#include "rgb.h"

struct Matrix
{
    quadRgb* entry;
    
    void poopingPacman(quadRgb *a, int pills);
    void swap(quadRgb &a, quadRgb &b);
    void swap(int &a, int &b);
    int  idx(int row, int col);

    // helpers for cycles transpose
    int calcNextIndex(int inputIndex);
    bool* swapped;

  public:
    int rows, cols, numSwaps;
    
    Matrix(quadRgb* entry,
           int rows,
           int cols);

    int  transpose(void);
    int  sqrTranspose(void);
    int  cyclesTranspose();
    void print();
};

bool operator==(const Matrix& lhs, const Matrix& rhs);
