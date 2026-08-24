#include<stdio.h>

char even(int a)
{
    if (a % 2 == 0)
    {
        return 1;
    }
    else {
        return 0;
    }


}

int main()
{
    int number;

    printf("Please Enter The Number : ");
    scanf("%d", &number);

    if (even(number) == 1)
    {
        printf("ZOAJ");
    }
    else {
        printf("FARD");
    }

    return 0;
}
