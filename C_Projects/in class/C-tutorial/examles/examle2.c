#include<stdio.h>

int main()
{
    int number;

    printf("Please Enter The Number: ");
    scanf("%d", &number);

    if (number > 20 && number < 200)
    {
        printf("OK");
    }

    return 0;
}
