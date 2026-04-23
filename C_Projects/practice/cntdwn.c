#include<stdio.h>

int countDown(int a)
{
    for (int i = a; i >= 0; i--)
    {
        if (i != 0)
        {
            printf("%d\n", i);
        }
        else if (i == 0)
        {
            printf("BOOM!\n");
        }
    }
    //printf("BOOM!");
}

int main()
{
    /*int b = countDown(9);

    printf("%d", b);*/
    int b;
    printf("enter number : ");
    scanf("%d", &b);

    countDown(b); // توی این خط هم دو سه روز درگیرش بودم چون یه مقدار رندوم بعد از بووم بیرون می‌داد بازم از دیپ سیک پرسیدم و گفت printf نباید داشته باشه

    return 0;
}