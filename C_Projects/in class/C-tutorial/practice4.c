#include<stdio.h>

int sumsum(int a)
{
    int b = a * a * a;
    //return a * a * a;
    printf("%d", b);
}

int main()
{
    /*
    int a = sumsum(5);

    printf("%d", a);
    */
    int a = 0;

    printf("Enter a number : ");
    scanf("%d", &a);

    sumsum(a);

    return 0;
}
