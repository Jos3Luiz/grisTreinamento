#include <stdio.h>

int soma(int n1,int n2){
	
	return n1+n2;
}


int main(){
	
	int a;
	int b;
	int c;

	a=3;
	b=2;

	c=soma(a,b);
	printf("a soma de %i+%i = %i\n",a,b,c);

	return 0;
}
