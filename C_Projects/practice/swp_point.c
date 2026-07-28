#include<stdio.h>

int main()
{
    int a = 20;
    int b = 66;

    int* p1;
    int* p2;

    p1 = &a;
    p2 = &b;
    printf("a = %d, b = %d \n", a, b);
    printf("*p1 = %d, *p2 = %d \n", *p1, *p2); // نمایش مقدار اولیه قبل از جا به جایی

    // int* temp;
    // temp = p1; // جا به جایی
    // p1 = p2; // جا به جایی
    // p2 = temp; // جا به جایی

    p1 = p1 + *p2; // جا به جایی بدون متغیر اضافی 
    p2 = p1 - *p2; // جا به جایی بدون متغیر اضافی 
    *p1 = p1 - p2; // جا به جایی بدون متغیر اضافی 
    printf("a = %d, b = %d \n", a, b);
    printf("*p1 = %d, *p2 = %d \n", *p1, *p2); // نمایش مقدار نهایی بعد از جا به جایی


    return 0;
}

// Amirhossein Arab Pour