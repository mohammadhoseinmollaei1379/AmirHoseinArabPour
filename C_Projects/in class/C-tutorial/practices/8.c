#include<stdio.h>
#include<math.h>

int main()
{
    /*
    char a[10] = "Goal";

    for(int i = 0; i < 10; i++)
    {
        printf("%d ", a[i]); // نمایش 0 0 0 0 0 یا عدد رندوم
    }
    int a[10] = {10, 11, 65, 72};
    for(int i = 0; i < 10; i++)
    {
        printf("%b ", a[i]); // نمایش 0 0 0 0 0 یا عدد رندوم
    }

    int x = sqrt(100); // جذر و رادیکال میگیره
    printf("%d\n", x);
    int y = pow(10, 4); // به توان میرسونه
    printf("%d\n", y);*/
    int x = 0;

    int* p; // متغیر اشاره گر
    p = &x;


    printf("%p", p);
    return 0;
}
