
struct Matrix
{
    int rows, cols;
    int* entry;
    
    void shift(int *a, int steps);
    void swap(int &a, int &b);
    int  idx(int row, int col);

  public:
    Matrix(int* entry,
           int rows,
           int cols);

    void inverse(void);
    void print();
};

bool operator==(const Matrix& lhs, const Matrix& rhs);
