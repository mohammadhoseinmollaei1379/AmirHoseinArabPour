#include<stdio.h>

int main()
{
    int number;

    printf("Please Enter The PASSWORD : ");
    scanf("%d", &number);

    switch(number)
    {
    case 14:
        printf("MAHDI");
        break;
    case 110:
        printf("ALI");
        break;
    default:
        printf("ERROR!");
        break;
    }
    /*if (number == 14)
    {
        printf("MAHDI");
    }
    else if (number == 110)
    {
        printf("ALI");
    }
    else {
        printf("ERROR!");
    }*/

    return 0;
}
