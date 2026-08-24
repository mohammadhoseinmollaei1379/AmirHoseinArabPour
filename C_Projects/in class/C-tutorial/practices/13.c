#include<stdio.h>
#include<string.h>
#define ali 200 // => تعریف یک متغیر کانست ولی با آن فرق دارد

int main()
{
    struct Student // تعریف یک استراکچر
    {
        int id;
        float grade;
        char first_name[20];
        char last_name[80];
    }; // => باید حتما انتهای یک استراکچر سمی کالن بذاریم

    struct Student stu1; // => تعریف یک متغیر از روی استراکچر دانش آموز
    stu1.id = 1020; // مقدار آیدی برابر با 1020
    stu1.grade = 19.5;
    strcpy(stu1.first_name, "ali"); // باید اینجوری مقدار دهیم
    strcpy(stu1.last_name, "alizadeh"); // باید اینجوری مقدار دهیم

    printf("%d", ali); // چاپ کردن دیفاین

    return 0;
}
