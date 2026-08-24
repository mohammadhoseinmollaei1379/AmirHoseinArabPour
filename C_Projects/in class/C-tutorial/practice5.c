#include<stdio.h>

void* swappp(int x, int y, int w)
{
    w = x;
    x = y;
    y = w;

}

int main()
{
    int x = 10;
    int y = 20;
    int z = swappp(x, y);

    printf("%d", z);

    return 0;
}

