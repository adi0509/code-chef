#include<stdio.h>
//using namespace std;
static unsigned long a[1000000000]={0}; //this line will initialise full array with 0.
unsigned long getCoin(unsigned long x)
{
	if(x<12)
		{
			return x;
		}
	if(x<1000000000)
		if(a[x]!=0)
			return a[x];
	
		int result=getCoin(x/2)+getCoin(x/3)+getCoin(x/4);
		if(x<1000000000)
			if(a[x]==0)
				a[x]=result;
		return result;
	
}
int  main()
{
	unsigned long x;
	while(true)
	{
		scanf("%lu",&x);
		if(x>0 && x<1000000000)
		printf("%lu\n",getCoin(x));
	}
	return 0;
}
