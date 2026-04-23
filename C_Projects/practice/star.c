#include<stdio.h>

char star(int a)
{
    for (int i = a; i > 0; i--)
    {
        printf("*");
    }
    
}

int main()
{
    //printf("%c", star(50));
    int st = 0;

    printf("enter the num : ");
    scanf("%d", &st);
    
    star(st);

    return 0;
}