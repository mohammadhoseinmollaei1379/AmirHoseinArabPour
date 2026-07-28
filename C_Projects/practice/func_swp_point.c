#include<stdio.h>

void swap_pointers(int** a, int** b)
{
    printf("*p1 = %d, *p2 = %d \n", *a, *b);

    int* temp; // جا به جایی 
    temp = *a; // جا به جایی 
    *a = *b; // جا به جایی 
    *b = temp; // جا به جایی 

    printf("*p1 = %d, *p2 = %d \n", *a, *b);
}

int main()
{
    int num1 = 10;
    int num2 = 20;

    int* p1;
    int* p2;

    p1 = &num1;
    p2 = &num2;

    int** pp1;
    int** pp2;

    pp1 = &p1;
    pp2 = &p2;

    swap_pointers(pp1, pp2);

    return 0;
}

// Amirhossein Arab Pour