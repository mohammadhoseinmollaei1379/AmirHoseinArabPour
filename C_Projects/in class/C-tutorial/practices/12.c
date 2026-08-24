#include<stdio.h>
#include<string.h>

int main()
{
    FILE *file1; // ساخت یک متغیر فایل
    char a[100];
    file1 = fopen("d:\\amir.txt", "r"); // باز کردن فایل با مسیر رو به رو
    /*
    att W = Write + delete
    att R = Read
    att A = attack => (Write - delete)
    att WB = write binary
    att RB = read binary => for picture
    */
    //fprintf(file1, "Hello World!"); // نوشتن در فایل با حذف محتوای قبل به دلیل اتریبیوت W
    fgets(a, 100/*تعداد 100 کاراکتر را می خواند*/, file1);
    printf(a); // می توانیم درصد اس نذاریم
    fclose(file1); // بستن فایل برای جلوگیری از مشکلات احتمالی
    /*
    char n[10] = "Good Bye";
    int a = strcspn(n, "y"); => باید حتما داخل دابل کوتیشن باشه
    n[a] = 'H'; => جا به جایی وای با اچ
    ------------------------------------------
    char m[100];
    scanf("%s \n", m); => نباید که اپرسند بذاریم برای متغیر استرینگ
    */

    return 0;
}

/*
تابع ها برای فایل ها
fwrite(nam motaghayyer ya reshteh, tool motaghayyer ya reshteh => ya => strlen(nam motaghayyer ya reshteh), tool yek karakter => ya => sizeof(char), nam file);
^
|
fwrite(a, strlen(a), sizeof(char), file1);
------------------------------------------
fwrite(nam motaghayyer ya reshteh, toolmeghdare khandani => ya => strlen(nam motaghayyer ya reshteh), tool yek karakter => ya => sizeof(char), nam file);
^
|
fwrite(a, strlen(a), sizeof(char), file1);
------------------------------------------
fgets(a, 100, file1);
------------------------------------------
fprintf(file1, "STRING");
*/
