#include <stdio.h>
int main(void)
{
	int ary[10];
	int i,j;
	int remainder[10] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
	int temp = 0;
	int count = 0;
	
	for (i = 0; i < 10; i++)
	{
		 scanf("%d", &ary[i]); 
	} 
	
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			if (ary[i]%42 == remainder[j])
			{
				temp = 1;
			}
		}
		if (temp == 0)
		{
			remainder[i] = ary[i]%42;
		}
		temp = 0;	
	}
	for (i = 0; i < 10; i++)
	{
		if (remainder[i] != -1)
		{
			count += 1;
		}
	 } 
	 
	 printf("%d", count);
	 
	 return 0;
}