#include<stdio.h>

void sortTwo(int* a, int* b)
{
    printf("%d %d \n", *a, *b);
    if (*a > *b)
    {
        int w;
        w = *a;
        *a = *b;
        *b = w;
    }
    printf("%d %d \n", *a, *b);
}

int main()
{
    int am = 20;
    int bm = 10;
    int* ab = &am;
    int* bc = &bm;

    sortTwo(ab, bc);

    return 0;
}

// Amirhossein Arab Pour