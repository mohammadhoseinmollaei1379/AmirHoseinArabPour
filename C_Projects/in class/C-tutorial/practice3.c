#include<stdio.h>

int main()
{
    char x;
    char y = "01000001";
    printf("enter password ");
    scanf("%d", &x);

    if (x == y){
        printf("welcome");
    }
    else{
        printf("ERROR");
    }

    return 0;
}
