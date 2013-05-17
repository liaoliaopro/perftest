#include "t.h"

int main(int argc, char const* argv[])
{
    int len = atoi(argv[1]);
            
    for (int i=0; i < len; i++)
    {
        A a={0,0};
        func(&a, 1);
    }

    return 0;
}
