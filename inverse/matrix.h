
struct Matrix
{
    int rows, cols;
    int* entries;
    
  public:
    Matrix(int* entries,
           int rows,
           int cols);

    void inverse(void);
};

bool operator==(const Matrix& lhs, const Matrix& rhs);
