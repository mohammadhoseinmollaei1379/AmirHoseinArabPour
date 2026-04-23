#include<stdio.h>

float number(int a, int b, int c)
{
    int x = a + b + c;
    float y = x / 3;

    return y;
}

int main()
{
    /*int num1 = 20;
    int num2 = 11;
    int num3 = 65;
    float num4 = number(num1, num2, num3);

    printf("%f \n", num4); مقدار معینی به این تابع می‌دهیم(خودمان)*/

    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    printf("enter a number 1: ");
    scanf("%d", &num1);
    printf("enter a number 2: ");
    scanf("%d", &num2);
    printf("enter a number 3: ");
    scanf("%d", &num3);


    float num4 = number(num1, num2, num3);
    printf("meghdar nahaaei : %f", num4);

    return 0;
}