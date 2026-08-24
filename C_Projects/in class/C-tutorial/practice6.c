#include<stdio.h>


int main()
{
    /*
    int x = 10;
    int y = 20;
    int z;

    printf("x = %d, y = %d\n", x, y);

    z = x;
    x = y;
    y = z;

    printf("x = %d, y = %d\n", x, y);
*/
    int x = 15;
    int y = 29;

    printf("x = %d, y = %d\n", x, y);

    y = x + y;
    x = y - x;
    y = y - x; // جا به جایی دو متغیر بدون متغیر اضافی

    printf("x = %d, y = %d\n", x, y);
    return 0;
}
