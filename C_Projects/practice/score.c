#include<stdio.h>

int main()
{
    int lesson = 0;
    float les = 0;
    float num_scr = 0;
    
    printf("Enter your lessons : ");
    scanf("%d", &lesson);

    for (int i = lesson; i >= 0; i--)
    {
        if (i == 0)
        {
            num_scr = num_scr / lesson;
            printf("your moaddel : %f", num_scr);
        }
        else{
        printf("enter score lesson %d : ", i);
        scanf("%f", &les);
        num_scr += les;
        }

    }
    

    return 0;
}