#include<stdio.h>
//using namespace std;
static unsigned long a[1000000000]={0}; //this line will initialise full array with 0.
unsigned long getCoin(unsigned long x)
{
	if(x<12)
		{
			return x;
		}
	else
	{
		if(a[(x/2)]==0)
			a[(x/2)]=getCoin(x/2);
		if(a[(x/3)]==0)
			a[(x/3)]=getCoin(x/3);
		if(a[(x/4)]==0)
			a[(x/4)]=getCoin(x/4);
		return a[(x/2)] + a[(x/3)] + a[(x/4)];
	}
}
int  main()
{
	unsigned long x;
	int i=0;
	while(i<2)
	{
		scanf("%lu",&x);
		if(x>0 && x<1000000000)
		printf("%lu\n",getCoin(x));
		i++;
	}
	return 0;
}