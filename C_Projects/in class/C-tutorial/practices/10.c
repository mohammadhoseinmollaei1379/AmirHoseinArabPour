#include<stdio.h>

void swap_pointer(int** p, int** q)
{
    int* temp;
    temp = *p;
    *p = *q;
    *q = temp;
}

int main()
{
    /*
    int x = 30;
    int y = 10;
    printf("x = %d, y = %d\n", x, y);
    int* p1;
    int* p2;
    p1 = &x;
    p2 = &y;

    int temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;

    printf("x = %d, y = %d\n", x, y); جا به جایی مقدار دو متغیر عددی

    int x = 30;
    int y = 10;
    int* p1;
    int* p2;
    p1 = &x;
    p2 = &y;
    printf("x = %d, y = %d\n", x, y);
    printf("*p1 = %d, *p2 = %d\n", x, y);

    int* temp;
    temp = p1;
    p1 = p2;
    p2 = temp;

    printf("x = %d, y = %d\n", x, y);
    printf("*p1 = %d, *p2 = %d\n", *p1, *p2);  جا به جایی مقدار دو متغیر اشاره گر
*/
    int x = 30;
    int y = 10;
    int* p1;
    int* p2;
    p1 = &x;
    p2 = &y;
    printf("x = %d, y = %d\n", x, y);
    printf("*p1 = %d, *p2 = %d\n", x, y);

    swap_pointer(&p1, &p2); // با استفاده از تابع

    printf("x = %d, y = %d\n", x, y);
    printf("*p1 = %d, *p2 = %d\n", *p1, *p2);

    return 0;
}
