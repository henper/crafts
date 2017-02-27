
struct Matrix
{
    int* entry;
    
    static void  poopingPacman(int *a, int pills);
    static void  swap(int &a, int &b);
    static void* threadEntryPoint(void*);
    
    void singleThreadedTranspose();
    void multiThreadedTranspose();
    int  idx(int row, int col);

  public:
    int rows, cols, numSwaps;
    
    Matrix(int* entry,
           int rows,
           int cols);

    void transpose(bool threaded = false);
    void print();
};

bool operator==(const Matrix& lhs, const Matrix& rhs);
