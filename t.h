typedef struct _A
{
    int age;
    double income;
}A;

typedef struct _B
{
    int total_age;
    double total_income;
}B;

B func(A *a, int len);
