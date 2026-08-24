#include <stdio.h>
#include <conio.h>
int main()
{
	/*
	for(int i=1; i<=10; i++)    
	{
		printf("%d\n", i);
	}
	
	for(int i=1; i<=10; i+=2)    
	{
		printf("%d\n", i);
	}
	for(;;)
	{
		printf("salam \n");       // == while true
	}
	
	int x = 1;
	while(x <= 10)
	{
		printf("salam \n");
		x++
	}*/
	for(int i = 1; i <= 10; i++)
	{
		printf("\n");
		for(int j = 1; j <= 10; j++)
		{
			printf("%3d  ", i * j);
		}
	}
	getch();
	return 0;
}