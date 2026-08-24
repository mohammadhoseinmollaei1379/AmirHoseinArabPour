#include<stdio.h>
#include<windows.h> // برای MESSAGEBOX

int y = 22; // =>  یک متغیر گلوبال یا همگانی

int main()
{
    int a = 5;
    int b = 10; // => متغری لوکال یا محلی
    /*
    printf("enter number :");
    scanf("%d", &a);

    if(a > 10 || || == OR a < 20)
    {
        printf("a = %d \n", a);
    }*/

    int z = a | b; // or می کند برای دو عدد
    int x = a & b; // and می کند برای دو عدد

    printf("%b", z);

    // MessageBox(NULL, "Hi", "Bye", MB_ICONQUESTION | MB_OKCANCEL); => برای دادن خروجی به صورت پنجره ای

    return 0;
}


/*
A | B | A || B          => OR
---------------
0 | 0 |    0
0 | 1 |    1
1 | 0 |    1
1 | 1 |    1

------------------------------

A | B | A && B          => AND
---------------
0 | 0 |    0
0 | 1 |    0
1 | 0 |    0
1 | 1 |    1

------------------------------

A | B | A ^ B           => XOR
---------------
0 | 0 |    0
0 | 1 |    1
1 | 0 |    1
1 | 1 |    0

------------------------------
*/
