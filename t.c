#include "t.h"

B func(A *a, int len)
{
    B b={0,0};
    for (int i = 0; i < len; i++) {
        b.total_age += a[i].age;
        b.total_income += a[i].income;
    }

    return b;
}

