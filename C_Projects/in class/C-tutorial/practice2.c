#include <stdio.h>

// این برنامه سر جلسه ی دوم تدریس زبان سی نوشته شده است
int main()
{
	int age = 42; // سن من
	float score = 19.5; // امتیاز من
	char grade = 'A';
	printf("i'm amir hossein. my age : %d ; my score is : %.2f ; my grade is : %c \n", age,  score, grade);
	score = 18.5;
	printf("%.2f  \n", score);
	printf("%.5f  \n", score);
	printf("%.3f  \n", score);
	return 0; // این دستور مهم است
}