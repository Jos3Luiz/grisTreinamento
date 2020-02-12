#include <stdio.h>
#define TARGET_MUST_PASS_IN_STACK true

int main()
{
	int idade=10;
	char nome[10]="carlos\0";
	printf("seu nome eh %s e sua idade eh %i\n",nome,idade);
	return 0;
}
