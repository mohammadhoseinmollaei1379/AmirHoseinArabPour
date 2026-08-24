#include<stdio.h>

int main()
{
    int a = 20;
    int b = 30;

    int* p1 = &a;
    int* p2 = &b;

    printf("*p1 = %d *p2 = %d \n", *p1, *p2);
    printf("p1 = %p p2 = %p \n", p1, p2);

    int* temp;
    temp = p1;
    p1 = p2;
    p2 = temp;

    printf("*p1 = %d *p2 = %d \n", *p1, *p2);
    printf("p1 = %p p2 = %p \n", p1, p2);


    return 0;
}
