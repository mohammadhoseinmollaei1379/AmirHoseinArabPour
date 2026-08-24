#include <stdio.h>

int main()
{
	int x = 10;
	int y;
	
	printf("plaese enter the number : ");
	scanf("%d", &y);
	
	if(y > x)
	{
		printf("bozorgtar \n");
	}
	if(y < x)
	{
		printf("koochektar \n");
	}
	/*if(y == x)
	{
		printf("mosavi \n");
	}*/
	else
	{
		printf("mosavi \n");
	}
	
	return 0;
}