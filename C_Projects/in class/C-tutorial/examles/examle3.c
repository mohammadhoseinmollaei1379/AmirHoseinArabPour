#include<stdio.h>

int main()
{
    int number1, number2, number3;

    int numbers[3];

    printf("Please Enter The Number 1 : ");
    scanf("%d", &number1);

    printf("Please Enter The Number 2 : ");
    scanf("%d", &number2);

    printf("Please Enter The Number 3 : ");
    scanf("%d", &number3);

        if (number1 > number2 && number1 > number3)
        {
            numbers[0] = number1;
        }
        if (number2 > number1 && number2 > number3)
        {
            numbers[0] = number2;
        }
        if (number3 > number2 && number3 > number1)
        {
            numbers[0] = number3;
        }
        if (number1 > number2 && number1 < number3)
        {
            numbers[1] = number1;
        }
        if (number2 > number1 && number2 < number3)
        {
            numbers[1] = number2;
        }
        if (number3 > number2 && number3 < number1)
        {
            numbers[1] = number3;
        }
        if (number1 < number2 && number1 < number3)
        {
            numbers[2] = number1;
        }
        if (number2 < number1 && number2 < number3)
        {
            numbers[2] = number2;
        }
        if (number3 < number2 && number3 < number1)
        {
            numbers[2] = number3;
        }
    printf("num 1 = %d, num 2 = %d, num 3 = %d", numbers[0], numbers[1], numbers[2]);

    return 0;
}
