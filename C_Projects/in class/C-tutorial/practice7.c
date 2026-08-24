#include<stdio.h>
#include<string.h>

int main()
{
    FILE *file1;
    char amir[11];
    file1 = fopen("d:\\amir.txt", "w");
    fprintf(file1, "HELLO WORLD");
    fclose(file1);
    file1 = fopen("d:\\amir.txt", "r");
    fread(amir, 11, sizeof(char), file1);
    amir[11] = '\0';
    printf(amir);
    fclose(file1);

    return 0;
}
