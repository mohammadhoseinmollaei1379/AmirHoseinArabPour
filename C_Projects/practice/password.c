#include<stdio.h>
#include<string.h>

char password(char a[10])
{
    while (0 == 0)
    {
        char b[10] = "salam";
        printf("enter your password : ");
        scanf("%s", a);
        if (!strcmp(b, a))
        {
            printf("Welcome!");
            break;
        }
    }
}

int main()
{
    char a[10];

    printf("%c", password(a));

    return 0;
}