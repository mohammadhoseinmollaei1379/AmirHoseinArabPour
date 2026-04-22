#include<stdio.h>

int mohasebeh(int a, int c, char b)
{
    if (b == '+')
    {
        printf("%d", a + c);
    }
    else if (b == '-')
    {
        printf("%d", a - c);
    }
    else{
        printf("ERROR! %c is not defined!", b);
    }
}

int main()
{
    /*int n1 = 12;
    int n2 = 25;
    char a = '+';

    int hasel = mohasebeh(n1, a, n2);

    printf("natijeh : %d \n", hasel); */

    int n1 = 0;
    int n2 = 0;
    char a;
    

    printf("enter a number 1 : ");
    scanf("%d", &n1);
    printf("enter a char : ");
    scanf("%c", &a);
    printf("enter a number 2 : ");
    scanf("%d", &n2);

    int n3 = mohasebeh(n1, a, n2);
    printf("hasel : %d", n3);

    return 0;
}