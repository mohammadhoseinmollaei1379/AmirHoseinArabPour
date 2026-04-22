#include<stdio.h>

char star(int a)
{
    for (int i = a; i > 1; i--)
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
    
    printf("%c", star(st));

    return 0;
}