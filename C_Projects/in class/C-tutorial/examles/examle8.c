#include<stdio.h>

int main()
{
    FILE *file1;

    char flname[25];
    printf("Please Enter The Full Name : ");
    scanf("%s", flname);

    file1 = fopen("C:\\Users\\SHEDco\\Desktop\\amir.txt", "w");
    fprintf(file1, flname);
    fclose(file1);

    return 0;
}
