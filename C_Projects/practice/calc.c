#include<stdio.h>

int mohasebeh(int a, char b, int c)
{
    if (b == '+')
    {
        int d = a + c;
        printf("%d", d);
    }
    else if (b == '-')
    {
        int d = a - c;
        printf("%d", d);
    }
    else{
        printf("ERROR! %c os not defined.", b);
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
    printf("enter a number 2 : ");
    scanf("%d", &n2);    
    printf("enter a char : ");
    scanf(" %c", &a); // توی این خط از دیپ سیک کمک گرفتم چون تا سه روز درگیرش بودم و باید یه فاصله قبل از %c می‌ذاشتم🤯

    mohasebeh(n1, a, n2);

    return 0;
}