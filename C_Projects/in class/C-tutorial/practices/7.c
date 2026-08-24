#include<stdio.h>
#include<string.h>
#include<conio.h>

int unic(char a)
{
    return (int)a;
}

int max(int d, int e)
{
    if(d > e){
        return d;
    }
    else if(d == e){
        return d;
    }
    else{
        return e;
    }
}

int main()
{
    /*int x[10];
    //x[0] = 234;
    for(int i = 0;i <= 9; i++)
    {
        x[i] = i + 10;
    }
    char y[20] = "Hello, World!";
    یادآوری جلسات قبل
    */

    /*char b[10] = "SALAM";
    strcpy(b, "HELLO"); // جایگزینی مقدار داده شده به مقدار قبلی در متغیر داده شده
    printf("%s \n", b);
    strcat(b, ", WORLD!"); // به مقدار قبلی در متغیر مقدار جدید را اضافه می کند
    printf("%s \n", b);
    char d[10] = "ROUND";
    char e[10] = "ROUND";
    int x = strcmp(d, e); // دو متغیر داده شده را مقایسه می کند و داخل متغیر ذخیره می کند
    printf("%d \n", x);*/
    int g, h;
    printf("enter the number 1 : ");
    scanf("%d", &g);
    printf("enter the number 2 : ");
    scanf("%d", &h);
    int f = max(g, h);
    printf("%d \n", f);
    //getch();
    /*printf("%d", unic('H'));
*/
    return 0;
}
