#include<stdio.h>

int countDown(int a)
{
    for (int i = a; i >= 0; i--)
    {
        if (i == 0)
        {
            printf("BOOM!");
        }
        else{
            printf("%d \n", i);
        }
    }
}

int main()
{
    /*int b = countDown(9);

    printf("%d", b);*/
    int b = 0;
    printf("enter number : ");
    scanf("%d", &b);

    printf("%d", countDown(b));

    return 0;
}