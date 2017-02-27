
struct Matrix
{
    int* entry;
    
    void poopingPacman(int *a, int pills);
    void swap(int &a, int &b);
    int  idx(int row, int col);

  public:
    int rows, cols, numSwaps;
    
    Matrix(int* entry,
           int rows,
           int cols);

    void transpose(void);
    void print();
};

bool operator==(const Matrix& lhs, const Matrix& rhs);
