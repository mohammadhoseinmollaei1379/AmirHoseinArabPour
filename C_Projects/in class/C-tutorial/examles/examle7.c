#include<stdio.h>
#include<windows.h>
#include<string.h>

int main()
{
    char fname[20];
    char lname[30];

    char flname[50];

    printf("Please Enter The First Name : ");
    scanf("%s", fname);
    printf("Please Enter The Last Name : ");
    scanf("%s", lname);

    strcat(flname, fname);
    strcat(flname, " ");
    strcat(flname, lname);

    MessageBox(NULL, flname, "first name & last name", MB_OK);

    return 0;
}
