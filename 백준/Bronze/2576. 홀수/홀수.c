#include <stdio.h>
int main(void)
{
	int i;
	int ary[7];
	int temp;
	int count = 0;
	int total = 0;
	int min;
	
	for (i = 0; i < 7; i++)
	{
		scanf("%d", &temp);
		if (temp%2 == 1)
		{
			ary[count] = temp;
			count += 1; 
		}
	 }
	 
	 min = ary[0];
	 
	for (i = 0; i < count; i++)
	{
		total += ary[i];
		if (ary[i] < min)
		{
			min = ary[i];
		}
	 }
	 
	if (count == 0)
	{
		printf("%d", -1);
	 } 
	else
	{
	 printf("%d\n", total);
	 printf("%d", min);
	}
	 return 0;
 } 