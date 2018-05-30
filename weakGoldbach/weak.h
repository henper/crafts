
typedef struct weakGoldbachNumbers
{
  int numbers[3];
  int sum() {return( numbers[0] + numbers[1] + numbers[2]); }
} weakGoldbachNumbers;

weakGoldbachNumbers calculateWeakGoldbachFor(int number);
