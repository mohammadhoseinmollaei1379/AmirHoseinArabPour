#include<stdio.h>

void pow(int x, int* t)
{
    *t = x * x; // مقدار x به توان دو را در مقدار متغیری که آدرسش را داریم میریزد
}

int main()
{
    /*
    int x = 20;
    int* p; // متغیر اشاره گر
    p = &x; // عملگر & برای آدرسدهی

    printf("x = %d \n", x); // عملگر با مقدار اولیه

    *p = 30; // عملگر * برای مقداردهی

    printf("%p \n", p);
    printf("x = %d \n", x); // عملگر با مقدار ثانویه
    printf("*p = %d \n", *p); // مقدار متغیر x که آدرسش در p ذخیره شده است
    */
    //int* x == int *x
    int x = 3;
    int k = 0;
    pow(x, &k);
    printf("k = %d \n", k); // نمایش خروجی

    return 0;
}
