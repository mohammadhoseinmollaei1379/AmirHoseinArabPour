#include<stdio.h>

int main()
{
    int x = 10;
    int y = 20;
    int z = 0;

    printf("x : %d , y : %d \n", x, y);

    z = x;
    x = y;
    y = z;

    printf("new x : %d , new y : %d", x, y);

    return 0;
}